# Lab 06 project rules

- REQUIREMENTS.md is the source of truth for late_fee's requirements.
- Keep REQUIREMENTS.md and fees.py unchanged.
- Use only the Python standard library.
- Tests use unittest, live in tests/, and import the function with:
  from fees import late_fee
- The student runs tests from lab06 with:
  python3 -m unittest discover -s tests
- Follow the active permission profile. Do not broaden permissions or run
  commands outside the sandbox.
- The tester derives tests from requirements, creates tests/test_fees.py,
  and stops without running tests or reading fees.py.
- The reviewer reads requirements and code, does not read tests/,
  replies with its findings, and changes no files.

