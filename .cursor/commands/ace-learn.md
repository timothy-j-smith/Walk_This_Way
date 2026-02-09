# ACE Learn

Capture learning from a completed task to improve future AI assistance.

## Action Required

Use the `ace_learn` MCP tool to capture what was learned:

```
ace_learn(
  task: "Brief description of what was done",
  trajectory: "Key steps taken during the task",
  output: "Important lessons, patterns, or insights discovered",
  success: true
)
```

## Example

After implementing a feature:
```
ace_learn(
  task: "Implemented JWT authentication",
  trajectory: "1. Added auth middleware 2. Created login endpoint 3. Added token refresh",
  output: "Always use httpOnly cookies for refresh tokens. Access tokens should be short-lived (15min).",
  success: true
)
```

## When to Use

- After completing a significant task
- When you discovered something important
- After fixing a tricky bug
- When a pattern worked well (or didn't)