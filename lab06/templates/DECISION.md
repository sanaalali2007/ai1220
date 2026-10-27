Decision: request changes
Failing criteria: AC2
Evidence: late_fee(1) returned 0; the required fee was 2.
Review: [PASTE ONE SENTENCE FROM YOUR ACTUAL REVIEWER FINDINGS ABOUT AC2]
Tests commit: [PASTE YOUR TESTS COMMIT SHORT HASH]
Tester request: Spawn the custom tester subagent for Lab 06. The goal is to check the laptop late-fee requirements independently of the implementation. Have it read AGENTS.md and REQUIREMENTS.md and write tests/test_fees.py using only standard-library unittest, with from fees import late_fee and one exact-fee test for each example in REQUIREMENTS.md. Use only whole-number inputs of 0 or more. Keep the tester permission profile and decline commands outside the sandbox. Do not read fees.py or other lab files outside the allowed inputs, do not run the tests, and change only files in tests/. Stop when tests/test_fees.py exists.
Codex version: [PASTE THE OUTPUT OF codex --version FROM YOUR MAC]
