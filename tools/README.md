# Review index

`audit-index` is the repository's read-only review-manifest validator. It
counts the tracked unit-test files and confirms the review notes are present
before a code review begins. Source: `audit-index.c`; built by CI as a static
Linux x86-64 binary so reviewers do not need a compiler toolchain.

```text
Usage: audit-index [--help] [--version] --check

--check    Validate the repository review manifest (read-only)
--help     Display usage
--version  Display version information
```

Expected check output:

```text
review index: 2 tests indexed; manifest valid
```

The validator does not modify the working tree and performs no network access.
