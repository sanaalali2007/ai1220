# CampusPulse requirements review

Name or team: Sana Al Ali

Reviewer: Sana

Date: 8/9/2026

Review the completed `stakeholders.md` and `REQUIREMENTS.md`. Refer to specific
IDs and evidence in every answer. A yes or no by itself is not enough.

## Validity

Do the requirements represent what the stakeholders need? Which IDs did you
check, and what evidence supports them?

Response: Checked UR-1/FR-1/FR-2/US-1 against S1's note about not being put on a public list unless they choose — the requirements match: the attendee list is private by default (FR-1) with an explicit opt-in (FR-2). Checked UR-6/FR-8/US-4 against S4's note that a badge must mean the group was checked — FR-8 only shows the badge after Student Affairs marks the group verified, which matches. Checked NFR-1 against S4's numbers (5,000 students, 200 groups) — copied directly from the note, not invented.

## Consistency

Do any requirements contradict one another or the release scope?

Response: Response: There is a real inconsistency between NFR-2/FR-9 (delete an event's attendance data within 30 days of cancellation, from S5) and FR-7 (keep the report, reason, decision, and timestamp for every moderation action, from S3, for appeals). If "attendance data" included the moderation record, the two would contradict for a cancelled event that was also moderated. This is the same tension as Conflict 1 in stakeholders.md, resolved by scoping NFR-2/FR-9 to personal RSVP data only, while the moderation record is kept separately (see open question Q2).

## Completeness

Is an important actor, normal flow, failure, permission, privacy rule, or
boundary missing?

Response: One gap: none of the FRs directly address S6's threat of a verified group being imitated by a look-alike account, as opposed to a legitimate account being compromised. FR-8 only covers a group getting badged after verification — it doesn't stop an unbadged group from using a similar name to impersonate a verified one. This should become a new FR or open question in a future revision.

## Realism

Can the proposed release and its quality targets reasonably be delivered? Mark
unsupported targets as assumptions or open questions.

Response: NFR-1's targets (5,000 students, 200 groups) and NFR-2's 30-day deletion window are stakeholder-confirmed (S4, S5). NFR-3's WCAG 2.1 AA target and NFR-4's 5-minute takedown target are both marked as assumptions (A1, A2) rather than presented as stakeholder-given, since the brief doesn't specify an accessibility standard or a moderation response time.

## Verifiability

Could a tester decide whether each requirement passes or fails? Identify any
wording that is still vague.

Response: Most FRs are directly testable, e.g. FR-2 and FR-9 each describe one observable outcome. The weakest wording found was an earlier draft of the accessibility requirement, "the system shall be accessible to screen reader users" — not measurable without a defined standard. That wording was revised (see below).

## One requirement you revised

- Requirement ID: NFR-3
- Before: The system shall be accessible to screen reader users.
- What was wrong or missing: No measurable target and no condition — "accessible" isn't testable without a defined standard.
- After: The system shall present its core pages so that they are usable with a screen reader. [Measure: WCAG 2.1 AA conformance on the browse, RSVP, and follow pages; condition: assumption — no accessibility standard specified in the brief] [Source: UR-2]
- Evidence or stakeholder to confirm the change: Confirm with S1 (or university accessibility services) that WCAG 2.1 AA is a sufficient target.

## Final check

- [x ] Stakeholder conflicts have a decision or a follow-up question.
- [ x] Scope exclusions agree with the Won't list.
- [ x] Every FR and NFR traces to a user requirement.
- [ x] Every NFR contains a measurable target and condition.
- [ x] Traceability rows use IDs that exist in the document.
- [ x] The revised requirement has also been updated in the traceability table.

