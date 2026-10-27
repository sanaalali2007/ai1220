# Lab 06: do the work in Terminal, then push to GitHub

This pack prepares Exercises 1 and 2 and gives you the steps for Exercise 3.
It is not a finished submission: the tester and reviewer sessions, permission
checks, version and Git hashes must come from your own Mac.

The worksheet requires the instructor's tested Codex build. If your version
differs, stop and ask your TA before running the sessions. Do not change
permissions to bypass a blocked command.

## 1. Put the lab in your existing repository

Extract this ZIP. Copy its **lab06 folder** into your existing private ai1220
repository. The result must include ai1220/lab06/fees.py.

If you already have a lab06 folder with work in it, merge the prepared settings
carefully instead of replacing your folder. Keep your original fees.py and
REQUIREMENTS.md. Do not copy reference/ or templates/ into the repository yet.

In Finder, press Cmd+Shift+. to show hidden files and confirm .codex and
.gitignore are present. The supplied .gitignore was not among the attachments;
this pack includes a replacement that ignores Python cache files.

Open Terminal, type `cd ` with a space, drag your **lab06 folder** into the
Terminal window and press Return. Then run:

```bash
pwd
git rev-parse --show-toplevel
ls
python3 --version
```

The first path should end in /ai1220/lab06, and the Git root should be your
ai1220 repository. All following commands run from lab06 unless stated
otherwise.

For a new lab, commit only the starter files first:

```bash
git add fees.py REQUIREMENTS.md README.md tests/README.md .gitignore
git diff --cached --name-only
git commit -m "Start lab06"
```

Check the staged list before the commit. If you already committed the starter
files unchanged, keep that commit and skip this step.

## 2. Check Codex and trust the folder

Run this alias line on its own:

```bash
alias codex=/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex
```

Then:

```bash
codex --version
```

Record the output. Compare it with the exact build announced by your instructor.
If it differs, or the executable is missing, ask the TA before continuing.
The worksheet explicitly requires this version check.

When the version matches:

```bash
codex
```

Trust this lab folder if prompted and sign in if asked. Then type:

```text
/quit
```

Repeat the alias line if you open a new Terminal window or tab.

## 3. Understand the prepared files

- AGENTS.md contains shared project rules.
- .codex/agents/tester.toml defines a tester that reads the requirements and
  writes tests, then stops without running them.
- .codex/agents/reviewer.toml defines a reviewer that reads the requirements
  and implementation, reports violations and changes nothing.
- .codex/config.toml grants the tester read access to AGENTS.md and
  REQUIREMENTS.md, plus read/write access to tests/. The reviewer gets read
  access to AGENTS.md, REQUIREMENTS.md and fees.py only.
- Both profiles disable command network access; web search is disabled.

The configuration follows the worksheet's outline, with explicit network-off
settings. Official permission syntax:
https://learn.chatgpt.com/docs/permissions

The configuration files have been parsed as TOML. Their permission enforcement
still needs the following checks on your Mac.

## 4. Run the worksheet's sandbox checks

Run commands one at a time and keep the observed results in your notes.
Do not start the tester or reviewer yet.

Each of these should print the file contents or x:

```bash
codex sandbox -- cat AGENTS.md
codex sandbox -- cat REQUIREMENTS.md
codex sandbox -- sh -c 'echo x > tests/check.txt && cat tests/check.txt'
codex sandbox -P reviewer -- cat AGENTS.md
codex sandbox -P reviewer -- cat fees.py
```

Each of these should be blocked, with Operation not permitted,
No such file or directory, or a network error:

```bash
codex sandbox -- cat fees.py
codex sandbox -- cat README.md
codex sandbox -- sh -c 'echo x >> fees.py'
codex sandbox -- curl -sS https://example.com
codex sandbox -P reviewer -- cat tests/check.txt
codex sandbox -P reviewer -- sh -c 'echo x >> fees.py'
```

A denied access attempt is a successful check of the restriction. A configuration
error, missing executable, or failure to start the sandbox does not show that
the restriction worked. Record the actual result and resolve setup problems
with your TA; do not approve an escape from the sandbox.

The two write-denial probes deliberately try to append x. Clean up:

```bash
rm tests/check.txt
git diff -- fees.py REQUIREMENTS.md
```

If a probe changed fees.py, record that permission check as FAIL, then restore
the committed original before continuing:

```bash
git restore fees.py
```

If REQUIREMENTS.md changed, restore the supplied original too. Do not mark a
check PASS just because the worksheet says it should pass.

## 5. Ask Codex to spawn the tester

From lab06:

```bash
codex
```

Paste this request into Codex:

```text
Spawn the custom tester subagent for Lab 06. The goal is to check the laptop late-fee requirements independently of the implementation. Have it read AGENTS.md and REQUIREMENTS.md and write tests/test_fees.py using only standard-library unittest, with from fees import late_fee and one exact-fee test for each example in REQUIREMENTS.md. Use only whole-number inputs of 0 or more. Keep the tester permission profile and decline commands outside the sandbox. Do not read fees.py or other lab files outside the allowed inputs, do not run the tests, and change only files in tests/. Stop when tests/test_fees.py exists.
```

The custom agent must be requested by name. Keep a copy of exactly what you
sent. Do not give the tester the code, the reference test file, or the results
later in this guide.

When the tester has finished and tests/test_fees.py exists, leave:

```text
/quit
```

If the file is missing, ask once more. After two unsuccessful attempts, the
worksheet permits you to write the tests yourself. The reference/test_fees.py
file is a checked example to understand and use for that fallback, not a claim
that a tester session has already happened. Record a fallback honestly in your
work.

## 6. Check the generated tests, run them, and commit

Compare the tests with REQUIREMENTS.md. There should be one exact-fee test
per example, using unittest and from fees import late_fee.

| Criterion | Minutes late | Exact required fee |
| --- | ---: | ---: |
| AC1 | 0 | 0 |
| AC2 | 1 | 2 |
| AC2 | 1440 | 2 |
| AC2 | 1441 | 4 |
| AC3 | 43200 | 20 |

Correct any wrong expected values and add missing examples. Do not add negative
or fractional inputs: those are outside this lab's stated input domain.

Run this yourself in normal Terminal, after quitting Codex:

```bash
python3 -m unittest discover -s tests
```

The supplied code should produce five tests with two failures: 1 minute returns
0 instead of 2, and 1441 minutes returns 2 instead of 4. These results were
verified using the separate reference tests in the assistant's workspace, not
your Mac. Record what your own run produces.

Keep fees.py unchanged. The failing tests expose the teammate's bug; they are
the evidence for this assignment.

Commit the tests and record the short hash:

```bash
git add tests
git commit -m "Add the tester's tests for late_fee"
git log -1 --format=%h
```

This is the **tests commit** for DECISION.md. The final submission hash later
will refer to a different commit.

## 7. Ask Codex to spawn the reviewer

Start a separate session with the reviewer profile:

```bash
codex -c 'default_permissions="reviewer"'
```

Paste:

```text
Spawn the custom reviewer subagent for Lab 06. Review late_fee by reading AGENTS.md, REQUIREMENTS.md and fees.py only. Keep the reviewer permission profile and decline commands outside the sandbox. Do not read tests/ or any other lab files and do not change any file. Reply with a list of every acceptance-criterion violation, giving the criterion, an example input, the fee the code returns and the required fee. Stop after that list.
```

Do not paste the tests or their results into the reviewer's session. Save the
actual reply and compare it with the test results after the review finishes.
Then leave with /quit.

The code uses floor division by 1440, so it drops any partial day. This breaks
AC2. For example, late_fee(1) is 0 instead of 2, and late_fee(1441) is 2 instead
of 4. AC1 and AC3 pass their supplied examples. The appropriate decision for the
supplied code is request changes.

This explanation is guidance, not a substitute for the required reviewer
session or its actual reply.

## 8. Complete the evidence and decision

From lab06, create the evidence folder:

```bash
mkdir -p evidence
```

Copy templates/sandbox-checks.txt from this pack to evidence/sandbox-checks.txt,
and copy templates/DECISION.md to lab06/DECISION.md.

In sandbox-checks.txt:
- Replace the version placeholder with your Mac's codex --version output.
- Replace every check placeholder with PASS only if you observed the required
  result; otherwise put FAIL followed by what happened.
- For lines combining two read probes, both must match the expected result.

In DECISION.md:
- Confirm the first three lines against your own run.
- Put one sentence from your actual reviewer's findings on the Review line.
- Insert the short tests commit hash and your actual Codex version.
- Make the Tester request line exactly match the prompt you actually sent.
- Keep the seven required lines; remove every placeholder.

No PASS results, Codex version, reviewer reply or commit hash have been invented
in the templates.

## 9. Commit, push and submit

Check that fees.py and REQUIREMENTS.md have no changes:

```bash
git diff -- fees.py REQUIREMENTS.md
git diff --cached -- fees.py REQUIREMENTS.md
git status --short
```

Remove tests/check.txt if it remains. Confirm these seven deliverables exist:
AGENTS.md, .codex/agents/tester.toml, .codex/agents/reviewer.toml,
.codex/config.toml, tests/test_fees.py, evidence/sandbox-checks.txt, DECISION.md.

Do not stage Codex session files or this help pack's reference/ and templates/
folders. Then use the worksheet's final commands:

```bash
cd ..
git add lab06
git diff --cached --name-only
git commit -m "Complete lab06 late fee checks"
git push
git rev-parse HEAD
```

Check the staged list before committing. Open your private repository on GitHub
and confirm the files are there, including .codex. Ensure the instructor or TA
has accepted the collaborator invitation and can access the repository.

Submit the repository URL and the final **full commit hash** through the LMS.
The ZIP is a preparation aid; it is not the lab submission.

