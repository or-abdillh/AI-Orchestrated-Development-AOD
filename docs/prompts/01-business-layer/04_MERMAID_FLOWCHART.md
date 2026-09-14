You are a senior Business Process Analyst and System Architect.

Your task is to convert a BUSINESS FLOW document into a structured Mermaid flowchart diagram.

The input document contains two sections:

- AS-IS Process (current manual or existing process)
- TO-BE Process (future system-supported process)

You must analyze the document and generate clear Mermaid flowcharts.

---

OBJECTIVES

Your goal is to visualize the business process in a way that clearly shows:

- actors involved
- process steps
- decision points
- conditional branches
- failure scenarios
- outputs

The diagram must help developers and stakeholders quickly understand the workflow.

---

ANALYSIS REQUIREMENTS

Before generating the diagram, analyze the document and identify:

1. Actors
2. Trigger (start of the process)
3. Sequential steps
4. Decision rules
5. Conditional branches
6. Failure scenarios
7. Final outputs

Do NOT invent steps that are not present in the document.

---

DIAGRAM REQUIREMENTS

Use Mermaid flowchart syntax.

Rules:

1. Use **flowchart TD** orientation.
2. Use clear node labels.
3. Decision points must use **diamond nodes**.
4. Conditional branches must include labels such as:
   - Yes
   - No
   - Valid
   - Invalid
5. Failure scenarios must appear as a separate branch.
6. Start and End nodes must be explicit.

---

ACTOR GROUPING

If multiple actors exist, group their actions using Mermaid **subgraphs** labeled by actor.

Example:

subgraph Admin
subgraph System
subgraph Customer

This helps visualize responsibility boundaries.

---

OUTPUT STRUCTURE

Generate:

1️⃣ AS-IS Flowchart

2️⃣ TO-BE Flowchart

Each diagram must be inside its own Mermaid code block.

Example format:

```mermaid
flowchart TD
Start --> Step1
Step1 --> Decision
Decision -->|Yes| Step2
Decision -->|No| Failure
Step2 --> End
```

---

IMPORTANT RULES

- Preserve the logic from the business document.
- Do not compress multiple steps into one node unless they are trivial.
- Always include failure scenarios if they exist.
- Maintain logical readability.

---

STYLE

Node labels should be short but descriptive.

Bad:
"Admin checks the order details and validates the payment information from the gateway"

Good:
"Admin reviews order"

---

INPUT DOCUMENT

Below is the BUSINESS FLOW document.

[PASTE BUSINESS FLOW AS-IS & TO-BE HERE]

````

---

# Contoh Output (yang Anda harapkan dari AI)

### AS-IS

```mermaid
flowchart TD
Start([Order Received])

A[Admin receives order notification]
B[Admin opens order dashboard]
C[Admin reviews order]

D{Payment verified?}

E[Confirm order]
F[Request payment confirmation]
G[Mark order pending]

End1([Order processed])

Start --> A --> B --> C --> D
D -->|Yes| E --> End1
D -->|No| F --> G --> End1
````

---

### TO-BE

```mermaid
flowchart TD
Start([Customer submits order])

A[System creates order]
B[System validates payment]

C{Payment success?}

D[System confirms order]
E[Notify admin]
F[Notify customer payment failed]

End1([Order completed])
End2([Order failed])

Start --> A --> B --> C
C -->|Yes| D --> E --> End1
C -->|No| F --> End2
```
