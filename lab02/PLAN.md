# Plan — LabLoans

## Process choice

### How stable and binding are the requirements?
The core need (check items in/out, see what's open) is unlikely to change much. The technician knows the workflow well and it's a small, well-understood problem.

### How quickly can real feedback arrive?
Very quickly — the technician uses the lab daily and can try each new feature within a day of it being ready.

### What does failure cost?
Low. A bug in a check-in/check-out record is inconvenient but not dangerous or expensive — it can be corrected manually if needed.

### How many pieces must move together?
Very few — one technician, one small tool, no integration with other systems required.

Verdict: Short increments (iterative/agile), not plan-driven.

## Milestones

| Milestone | When | What is true then |
|---|---|---|
| Basic checkout/checkin working | End of Sprint 1 | Technician can check an item out and back in, and see it reflected in the open-loans list |
| Loan history view added | End of Sprint 2 | Technician can search any item and see its past loan history |
| Pilot with real inventory | End of Sprint 3 | All lab equipment tracked through the system for one full week with no manual backup log |

## Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Technician doesn't have time to log every checkout during busy periods | Medium | Keep the checkout flow to the fewest possible fields (student ID, item, date) |
| Student ID lookups are slow or fail | Low | Allow manual name entry as a fallback |