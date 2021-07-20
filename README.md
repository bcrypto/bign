# Bign: digital signature and key transport algorithms based on elliptic curves

![](figs/bign-logo-small.png)

## What is Bign?

Bign is a digital signature system developed in 2010 and standardized a year
later in Belarus. The official standard STB 34.101.45 informally inherits the 
name Bign while the core signature system tends to be called `bign-sign`.

## BignV1

The `bign-sign` system follows the 
[Schnorr signature scheme](https://en.wikipedia.org/wiki/Schnorr_signature). 
By truncating the hash part of the signatures, `bign-sign` makes them quite short: 
48, 72, or 96 octets depending on the security level. 

Additionally to `bign-sign`, the first edition of STB 34.101.45 defines the 
following cryptographic mechanisms:
- `bign-curves` — elliptic curves as a cryptographic platform: 
   selection strategy, validation, standard curves for 3 security levels;
- `bign-keytransport` — key transport: public key encryption of symmetric keys.

`Bign-curves` are conventional Weierstrass curves over large prime finite fields. 
These curves are used outside of Bign to build protocols of the Diffie-Hellman 
type.

Bign allows using the same pair of private and public keys both in 
`bign-sign` and `bign-keytransport`. Thus, a single public key certificate
can serve both authenticity and confidentiality of the holder.

## BignV2

The second version of STB 34.101.45, released in 2013, additionally defines:
- `bign-genk` — an algorithm for generating ephemeral keys during signature 
  creation to make `bign-sign` fully deterministic;
- `bign-ibs` — a [Galindo-Garcia](https://link.springer.com/chapter/10.1007/978-3-642-02384-2_9)-like 
  identity-based signature system; 
- `PBKDF2` and `PBES2` — password-based mechanisms to protect Bign private keys. 

## What is this repo?

In this repo, we process comments on the current version of Bign,
discuss future versions, provide additional supporting material.

The latest releases of Bign can be found at 
[Releases](https://github.com/bcrypto/bign/releases).

Comments and proposals are processed at 
[Issues](https://github.com/bcrypto/bign/issues). 

