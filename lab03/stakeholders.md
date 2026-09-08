# CampusPulse stakeholder analysis

Name or team:

Date:

Read the stakeholder notes in the lab handout before completing this file.
Use the stakeholder types and power-interest quadrants from Week 2, Lecture 2.

Stakeholder types: end user, operations, business, regulator, negative stakeholder

Power-interest quadrants: key player, keep satisfied, keep informed, minimal effort

## S1

- Stakeholder: Student attendee
- Stakeholder type: end user
- Power-interest quadrant: keep informed
- Main goal:Keep up with club events and announcements in one place instead of checking email, Instagram, and group chats separately.
- Main concern: Being put on a public RSVP list without choosing to, and being able to use the app on a phone or with a screen reader.
- How you would involve or monitor this stakeholder:Test the RSVP and browsing flow with a few students, including someone who uses a screen reader, before launch.

## S2

- Stakeholder: Group officer
- Stakeholder type: end user
- Power-interest quadrant: key player
- Main goal: Post accurate event and announcement info for their group, with more than one officer able to help write it.
- Main concern: Only approved officers should be able to publish, and attendees need to be told if event details change.
- How you would involve or monitor this stakeholder: Have a few officers test the draft/publish workflow before launch, since they'll use it every day.

## S3

- Stakeholder: Campus moderator
- Stakeholder type: operations
- Power-interest quadrant: key player
- Main goal: Remove harmful or reported content quickly and keep a clear record for appeals.
- Main concern: Needing to hide an event immediately while still preserving the report, reasoning, and decision in case the group appeals.
- How you would involve or monitor this stakeholder: Involve moderators directly in designing the report/hide/appeal workflow, since they'll operate it daily.

## S4

- Stakeholder: Student Affairs
- Stakeholder type: business
- Power-interest quadrant: key player
- Main goal: Launch a verified-groups pilot (5,000 students, 200 groups) ready before Orientation Week.
- Main concern: The official badge must only appear on groups that have actually been checked, or it undermines trust in the badge.
- How you would involve or monitor this stakeholder: Regular check-ins as project sponsor, with sign-off on the verification process before release.

## S5

- Stakeholder: Data Protection Officer
- Stakeholder type: regulator
- Power-interest quadrant: keep satisfied
- Main goal: Ensure the service collects only the personal data it needs and removes it when no longer required.
- Main concern: RSVP lists must start private, and attendance data for a cancelled event must be deleted within 30 days.
- How you would involve or monitor this stakeholder: Get sign-off on the data-retention and deletion design before release.

## S6

- Stakeholder: Abuse cases (impersonators / compromised accounts)
- Stakeholder type: negative stakeholder
- Power-interest quadrant: minimal effort
- Main goal: Imitate a verified group to spread phishing events, or reuse a compromised account to spam announcements.
- Main concern: Preventing impersonation of verified groups and repeated abusive posting from a compromised account.
- How you would involve or monitor this stakeholder: Not consulted like a normal stakeholder — instead monitor through abuse-detection controls (badge checks, publish permissions, rate limits on repeat posts).

## Conflicts to resolve

Describe at least two real tensions. For each one, name both stakeholder IDs
and either propose a decision or write a specific question that should go back
to the stakeholders.

### Conflict 1

- Stakeholders: S3 (campus moderator) and S5 (Data Protection Officer)
- What conflicts: S3 needs to keep the report, reason, and decision behind a moderation action in case the group appeals. S5 requires that an event's attendance data be deleted within 30 days of cancellation. If "attendance data" includes the moderation record, the two requirements contradict each other.
- Proposed decision or follow-up question: Keep personal RSVP/attendance data and moderation-decision records as separate data. Delete the personal RSVP data within 30 days as S5 requires, but keep the moderation record (report, reason, decision, timestamp) without attendee names for as long as an appeal is possible. Follow-up question to S5: is a de-identified moderation record acceptable to keep past 30 days?

### Conflict 2

- Stakeholders: S2 (group officer) and S6 (abuse cases)
- What conflicts: S2 wants any officer to be able to start or continue drafting an announcement. S6's risk is a compromised account posting repeatedly, or an imitator publishing as a verified group — the more officers who can publish, the bigger that risk.
- Proposed decision or follow-up question: Let any officer draft or edit an announcement, but only officers with an "approved publisher" permission can actually publish it, and log who published each item. Follow-up question: should Student Affairs grant "approved publisher" status, or should the group's own admin officer assign it?

