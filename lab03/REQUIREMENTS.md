# CampusPulse requirements

Name or team: Sana Al Ali

Date: 8/9/2026

Status: working draft

Use the source IDs `S1` to `S6` from the lab handout. Keep every requirement
short enough to test and trace.

## 1. Release scope

### In scope

List at least three capabilities that belong in the first release.

- University sign-in (SSO) for all students and group officers
- Verified group profiles, announcements, and events, with follow, RSVP, and audience visibility (public vs. members-only)
- Corrections to published event/announcement details, with notification to attendees
- Reporting, moderation (including immediate hide), and appeals

### Out of scope

List at least two explicit exclusions.

- Direct messages between users
- External (non-university) users and payments
- Native mobile app, video hosting, and AI-driven recommendations

## 2. User requirements

Write at least five customer-readable needs. Use one need per line and trace it
to the stakeholder evidence.

Format: `UR-1 [Must] ... [Source: S1]`

- UR-1 [Must] Students can RSVP to an event without their name appearing on a public attendee list unless they explicitly choose to share it. [Source: S1]
- UR-2 [Must] Students can browse and RSVP to events and announcements using a screen reader and on a phone browser. [Source: S1]
- UR-3 [Must] Multiple officers of a group can draft an announcement together, but only an approved officer can publish it. [Source: S2]
- UR-4 [Must] Students who RSVP'd to an event are told if its date, time, or location changes. [Source: S2]
- UR-5 [Must] A campus moderator can hide a reported event immediately, while a record of the report and the decision is kept for any appeal. [Source: S3]
- UR-6 [Must] A group only shows an official verified badge after Student Affairs has checked and approved it. [Source: S4]
- UR-7 [Must] A student's personal RSVP/attendance data is collected only where needed and removed within 30 days after an event is cancelled. [Source: S5]

## 3. Functional requirements

Write at least six observable system behaviours. Start each one with "The
system shall" and trace it to one or more user requirements.

Format: `FR-1 [Must] The system shall ... [Source: UR-1]`

- FR-1 [Must] The system shall hide an attendee's identity from other users on an event's attendee list by default. [Source: UR-1]
- FR-2 [Must] The system shall let an attendee opt in to show their name on an event's public attendee list. [Source: UR-1]
- FR-3 [Must] The system shall present event and announcement pages with screen-reader-compatible labels and keyboard/touch navigation. [Source: UR-2]
- FR-4 [Must] The system shall let any officer of a verified group edit a draft announcement but shall only let an officer with "approved publisher" permission publish it. [Source: UR-3]
- FR-5 [Must] The system shall notify every student who RSVP'd to an event when its date, time, or location is edited. [Source: UR-4]
- FR-6 [Must]

## 4. Non-functional requirements

Write at least four measurable quality requirements. State what is measured,
the target, and the condition under which the target applies. If you introduce
a number that is not in the handout, record it as an assumption or open
question in Section 8.

Format: `NFR-1 [Must] The system shall ... [Measure: target and condition] [Source: UR-1]`

- NFR-1 [Must] The system shall support at least 5,000 registered student accounts and 200 verified group accounts. [Measure: 5,000 students / 200 groups, active without account-creation failures; condition: during the Orientation Week pilot] [Source: UR-6]
- NFR-2 [Must] The system shall remove an event's personal RSVP/attendance records after cancellation. [Measure: fully removed within 30 days of cancellation, for 100% of cancelled events; condition: applies university-wide] [Source: UR-7]
- NFR-3 [Should] The system shall make its core pages usable with a screen reader. [Measure: WCAG 2.1 AA conformance on the browse, RSVP, and follow pages; condition: assumption — no accessibility standard given in the brief] [Source: UR-2]
- NFR-4 [Must] The system shall remove a hidden event from public listings promptly after a moderator's decision. [Measure: hidden within 5 minutes of the moderator's action; condition: assumption — no response-time target given in the brief] [Source: UR-5]

## 5. User stories and acceptance criteria

Write at least three stories from different stakeholder viewpoints. Each story
needs at least two acceptance criteria. Across the set, include a failure,
permission boundary, privacy rule, or other non-happy path.

### US-1 [Source: S?, UR-?]

As a <role>,

I want <capability>,

so that <benefit>.

Acceptance criteria:

-
-

### US-2 [Source: S?, UR-?]

As a <role>,

I want <capability>,

so that <benefit>.

Acceptance criteria:

-
-

### US-3 [Source: S?, UR-?]

As a <role>,

I want <capability>,

so that <benefit>.

Acceptance criteria:

-
-

## 6. MoSCoW summary

List requirement or story IDs in every category. The Won't category must state
what is excluded from this release.

- Must:
- Should:
- Could:
- Won't this release:

## 7. Traceability

Add at least four complete paths. Every row should connect evidence to a user
requirement, a system requirement, and a user story.

| Stakeholder need | User requirement | System requirement | User story |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## 8. Assumptions and open questions

Separate decisions your team has assumed from questions that still need an
answer.

### Assumptions

- A1:

### Open questions

- Q1:
