load("@io_tweag_rules_haskell//haskell:haskell.bzl", "haskell_library")

haskell_library(
  name = "conduit",
  visibility = ["//visibility:public"],
  deps = [
    "@hackage_conduit//:conduit",
    "@hackage_http_client//:http-client",
    "@hackage_http_client_tls//:http-client-tls",
    "@hackage_monad_control//:monad-control",
    "@hackage_mtl//:mtl",
    "@hackage_resourcet//:resourcet",
  ],
  prebuilt_dependencies = [
    "base",
    "bytestring",
  ],
  srcs = [
    "Network/HTTP/Client/Conduit.hs",
    "Network/HTTP/Conduit.hs",
  ],
)

haskell_library(
  name = "http-conduit",
  visibility = ["//visibility:public"],
  deps = [
    ":conduit",
    "@hackage_aeson//:aeson",
    "@hackage_aeson//:core",
    "@hackage_aeson//:types",
    "@hackage_conduit//:conduit",
    "@hackage_conduit_extra//:conduit-extra",
    "@hackage_exceptions//:exceptions",
    "@hackage_http_client//:http-client",
    "@hackage_http_client_tls//:http-client-tls",
    "@hackage_http_types//:http-types",
    "@hackage_resourcet//:resourcet",
  ],
  prebuilt_dependencies = [
    "base",
    "bytestring",
    "transformers",
  ],
  srcs = [
    "Network/HTTP/Simple.hs",
  ],
)