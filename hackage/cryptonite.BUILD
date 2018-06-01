load("@io_tweag_rules_haskell//haskell:haskell.bzl", "haskell_library")

cc_library(
  name = "cbits",
  srcs = [
    "cbits/cryptonite_chacha.c",
    "cbits/cryptonite_salsa.c",
    "cbits/cryptonite_xsalsa.c",
    "cbits/cryptonite_rc4.c",
    "cbits/cryptonite_cpu.c",
    "cbits/ed25519/ed25519.c",
    "cbits/p256/p256.c",
    "cbits/p256/p256_ec.c",
    "cbits/cryptonite_blake2s.c",
    "cbits/cryptonite_blake2sp.c",
    "cbits/cryptonite_blake2b.c",
    "cbits/cryptonite_blake2bp.c",
    "cbits/cryptonite_poly1305.c",
    "cbits/cryptonite_sha1.c",
    "cbits/cryptonite_sha256.c",
    "cbits/cryptonite_sha512.c",
    "cbits/cryptonite_sha3.c",
    "cbits/cryptonite_md2.c",
    "cbits/cryptonite_md4.c",
    "cbits/cryptonite_md5.c",
    "cbits/cryptonite_ripemd.c",
    "cbits/cryptonite_skein256.c",
    "cbits/cryptonite_skein512.c",
    "cbits/cryptonite_tiger.c",
    "cbits/cryptonite_whirlpool.c",
    "cbits/cryptonite_scrypt.c",
    "cbits/cryptonite_pbkdf2.c",
  ],
  hdrs = glob(["cbits/**/*.h"]),
  includes = [
    "cbits",
    "cbits/blake2/argon2",
    "cbits/blake2/sse",
    "cbits/decaf/include/arch_ref64",
  ],
)

haskell_library(
  name = "cryptonite",
  visibility = ["//visibility:public"],
  deps = [
    ":cbits",
    "@hackage_foundation//:foundation",
    "@hackage_memory//:memory",
  ],
  prebuilt_dependencies = [
    "bytestring",
    "base",
    "integer-gmp",
    "ghc-prim",
    "deepseq",
  ],
  compiler_flags = [
    "-optc-O3",
    "-DSUPPORT_SSE",
  ],
  srcs = [
    "Crypto/Cipher/AES.hs",
    "Crypto/Cipher/Blowfish.hs",
    "Crypto/Cipher/Camellia.hs",
    "Crypto/Cipher/ChaCha.hs",
    "Crypto/Cipher/ChaChaPoly1305.hs",
    "Crypto/Cipher/DES.hs",
    "Crypto/Cipher/RC4.hs",
    "Crypto/Cipher/Salsa.hs",
    "Crypto/Cipher/TripleDES.hs",
    "Crypto/Cipher/Twofish.hs",
    "Crypto/Cipher/Types.hs",
    "Crypto/Cipher/Utils.hs",
    "Crypto/Cipher/XSalsa.hs",
    "Crypto/ConstructHash/MiyaguchiPreneel.hs",
    "Crypto/Data/AFIS.hs",
    "Crypto/Data/Padding.hs",
    "Crypto/ECC.hs",
    "Crypto/Error.hs",
    "Crypto/MAC/CMAC.hs",
    "Crypto/MAC/Poly1305.hs",
    "Crypto/MAC/HMAC.hs",
    "Crypto/Number/Basic.hs",
    "Crypto/Number/F2m.hs",
    "Crypto/Number/Generate.hs",
    "Crypto/Number/ModArithmetic.hs",
    "Crypto/Number/Prime.hs",
    "Crypto/Number/Serialize.hs",
    "Crypto/Number/Serialize/Internal.hs",
    "Crypto/KDF/Argon2.hs",
    "Crypto/KDF/PBKDF2.hs",
    "Crypto/KDF/Scrypt.hs",
    "Crypto/KDF/BCrypt.hs",
    "Crypto/KDF/HKDF.hs",
    "Crypto/Hash.hs",
    "Crypto/Hash/IO.hs",
    "Crypto/Hash/Algorithms.hs",
    "Crypto/OTP.hs",
    "Crypto/PubKey/Curve25519.hs",
    "Crypto/PubKey/Curve448.hs",
    "Crypto/PubKey/MaskGenFunction.hs",
    "Crypto/PubKey/DH.hs",
    "Crypto/PubKey/DSA.hs",
    "Crypto/PubKey/ECC/Generate.hs",
    "Crypto/PubKey/ECC/Prim.hs",
    "Crypto/PubKey/ECC/DH.hs",
    "Crypto/PubKey/ECC/ECDSA.hs",
    "Crypto/PubKey/ECC/P256.hs",
    "Crypto/PubKey/ECC/Types.hs",
    "Crypto/PubKey/ECIES.hs",
    "Crypto/PubKey/Ed25519.hs",
    "Crypto/PubKey/Ed448.hs",
    "Crypto/PubKey/RSA.hs",
    "Crypto/PubKey/RSA/PKCS15.hs",
    "Crypto/PubKey/RSA/Prim.hs",
    "Crypto/PubKey/RSA/PSS.hs",
    "Crypto/PubKey/RSA/OAEP.hs",
    "Crypto/PubKey/RSA/Types.hs",
    "Crypto/Random.hs",
    "Crypto/Random/Types.hs",
    "Crypto/Random/Entropy.hs",
    "Crypto/Random/EntropyPool.hs",
    "Crypto/Random/Entropy/Unsafe.hs",
    "Crypto/Tutorial.hs",
    "Crypto/Cipher/AES/Primitive.hs",
    "Crypto/Cipher/Blowfish/Box.hs",
    "Crypto/Cipher/Blowfish/Primitive.hs",
    "Crypto/Cipher/Camellia/Primitive.hs",
    "Crypto/Cipher/DES/Primitive.hs",
    "Crypto/Cipher/Twofish/Primitive.hs",
    "Crypto/Cipher/Types/AEAD.hs",
    "Crypto/Cipher/Types/Base.hs",
    "Crypto/Cipher/Types/Block.hs",
    "Crypto/Cipher/Types/GF.hs",
    "Crypto/Cipher/Types/Stream.hs",
    "Crypto/Cipher/Types/Utils.hs",
    "Crypto/Error/Types.hs",
    "Crypto/Number/Compat.hs",
    "Crypto/Hash/Types.hs",
    "Crypto/Hash/Blake2s.hs",
    "Crypto/Hash/Blake2sp.hs",
    "Crypto/Hash/Blake2b.hs",
    "Crypto/Hash/Blake2bp.hs",
    "Crypto/Hash/SHA1.hs",
    "Crypto/Hash/SHA224.hs",
    "Crypto/Hash/SHA256.hs",
    "Crypto/Hash/SHA384.hs",
    "Crypto/Hash/SHA512.hs",
    "Crypto/Hash/SHA512t.hs",
    "Crypto/Hash/SHA3.hs",
    "Crypto/Hash/Keccak.hs",
    "Crypto/Hash/MD2.hs",
    "Crypto/Hash/MD4.hs",
    "Crypto/Hash/MD5.hs",
    "Crypto/Hash/RIPEMD160.hs",
    "Crypto/Hash/Skein256.hs",
    "Crypto/Hash/Skein512.hs",
    "Crypto/Hash/Tiger.hs",
    "Crypto/Hash/Whirlpool.hs",
    "Crypto/Random/Entropy/Source.hs",
    "Crypto/Random/Entropy/Backend.hs",
    "Crypto/Random/ChaChaDRG.hs",
    "Crypto/Random/SystemDRG.hs",
    "Crypto/Random/Probabilistic.hs",
    "Crypto/PubKey/Internal.hs",
    "Crypto/PubKey/ElGamal.hs",
    "Crypto/ECC/Simple/Types.hs",
    "Crypto/ECC/Simple/Prim.hs",
    "Crypto/Internal/Proxy.hs",
    "Crypto/Internal/ByteArray.hs",
    "Crypto/Internal/Compat.hs",
    "Crypto/Internal/CompatPrim.hs",
    "Crypto/Internal/DeepSeq.hs",
    "Crypto/Internal/Imports.hs",
    "Crypto/Internal/Words.hs",
    "Crypto/Internal/WordArray.hs",
    "Crypto/Hash/SHAKE.hs",
    "Crypto/Hash/Blake2.hs",
    "Crypto/Internal/Nat.hs",
    "Crypto/Random/Entropy/RDRand.hs",
    "Crypto/Random/Entropy/Unix.hs",
  ],
)
