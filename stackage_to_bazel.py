#!/usr/bin/env python3

import yaml
import sys
import tarfile

build_plan = []

stack_path = '/home/ruuda/.stack'

def list_package_contents(name, version):
    prefix = f'{name}-{version}/'
    with tarfile.open(f'{stack_path}/indices/Hackage/packages/{name}/{version}/{name}-{version}.tar.gz') as tar:
        return [m.name[len(prefix):] for m in tar.getmembers()]


with open(stack_path + '/build-plan/lts-10.5.yaml', 'r') as lts_file:
    build_plan = yaml.load(lts_file)

core_packages = set(build_plan['system-info']['core-packages'].keys())
packages = build_plan['packages']

roots = sys.argv[1:]

done = set(list(core_packages))
todo = roots

f = open('stackage.bzl', 'w')

while todo:
    name = todo.pop()

    if name in done:
        continue

    package = packages[name]

    deps = []
    for dep, props in package['description']['packages'].items():
        if 'library' in props['components']:
            deps.append(dep)

    missing_deps = [dep for dep in deps if not dep in done]

    if missing_deps:
        todo.append(name)
        todo.extend(missing_deps)
        continue

    done.add(name)

    version = package['version']
    version_name = name + '-' + version
    target_name = name.replace('-', '_').replace('.', '_')
    repo_name = 'hackage_' + target_name
    sha256 = package['cabal-file-info']['hashes']['SHA256']

    prebuilt_deps = [f'\n    "{dep}",' for dep in deps if dep in core_packages]
    prebuilt_deps_str = ''.join(prebuilt_deps)

    hackage_deps = []
    for dep in deps:
        if dep in core_packages:
            continue
        dep_repo_name = dep.replace('-', '_').replace('.', '_')
        hackage_deps.append(f'\n    "@hackage_{dep_repo_name}//:{dep}",')
    hackage_deps_str = ''.join(hackage_deps)

    package_contents = list_package_contents(name, version)
    modules = package['description']['modules']
    root_modules = set(mod.split('.')[0] for mod in modules)
    source_files = [src for src in package_contents if src.endswith('.hs')]

    if 'src' in package_contents:
        src_prefix = 'src/'
        # If these is an 'src' directory, take *only* the src directory. This is
        # to deal with the 'transformers-compat' package, which also has other
        # directories that are unused.
        source_files = [src for src in source_files if src.startswith('src/')]
    else:
        src_prefix = ''

    # Hack: try to find all hs files that define the module, but not tests or
    # other auxillay hs files in the tarball.
    sources = []
    for src in source_files:
        mod = src.split('/')[1 if src_prefix else 0]
        if not mod in root_modules:
            # Might have been a Setup.hs, a test file, or some other auxillary
            # file.
            continue
        # Hack: ansi-terminal contains an example and Windows files that we
        # exclude.
        if ('Windows' in src) or (src.endswith('Example.hs')):
            continue

        sources.append(f'\n    "{src}",')

    sources_str = 'srcs = [' + ''.join(sources) + '\n  ],'
    if src_prefix:
        sources_str += '\n  src_strip_prefix = "src",'

    if 'includes' in package_contents:
        # ansi-terminal has includes and needs defines. Hack it together like
        # this, and hope that this does not mess up other packages too badly.
        header_fnames = [f'\n    "{h}",' for h in package_contents
                         if h.startswith('includes') and h.endswith('.hs')]
        headers = '\n  hdrs = [' + ''.join(header_fnames) + '\n  ],'
        cflags = '\n  compiler_flags = ["-DUNIX"],'
    else:
        headers = ''
        cflags = ''

    print(version_name, '=>', '@' + repo_name)

    build_def = f'''
new_http_archive(
  name = "{repo_name}",
  urls = [
    # Note: Hackage can serve a file with a different hash than what the
    # Stackage snapshot specifies. But fpco mirrors time out.
    "https://hackage.haskell.org/package/{version_name}/{version_name}.tar.gz",
    "https://s3.amazonaws.com/hackage.fpcomplete.com/package/{version_name}.tar.gz",
  ],
  # sha256 = "{sha256}",
  strip_prefix = "{version_name}",
  build_file_content = """
load("@io_tweag_rules_haskell//haskell:haskell.bzl",
  "haskell_library",
  "haskell_toolchain",
)

haskell_library(
  name = "{name}",{headers}
  visibility = ["//visibility:public"],
  {sources_str}
  deps = [{hackage_deps_str}
  ],
  prebuilt_dependencies = [{prebuilt_deps_str}
  ],{cflags}
)
  """,
)'''
    print(build_def, file=f)
