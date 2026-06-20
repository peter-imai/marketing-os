# `/new-project` Roadmap

V2+ ideas. Stays local until mature enough to promote to `_system/backlog.md`.

---

## V2 Ideas

- **Deep-path routing.** After scaffold, offer: "Want to do full positioning now?" → routes to `/positioning` (Dunford). "Want market research?" → routes to Crawford prompts. Currently just suggests these as next steps.
- **Template library.** Different project types (SaaS, agency client, e-commerce, personal brand) could seed different marketing-strategy sections and activity routing tables.
- **Batch onboarding.** "I have 4 clients to set up" → streamlined flow that asks shared questions once (B2B/B2C, multi-project context) then iterates per project.
- **Import from external system.** If the operator has existing context (Notion, Google Docs, Cursor), offer to import and triage into the canonical doc structure. Related: `_system/client-context-architecture.md` § Importing from External Systems.
- **Plugin packaging.** If/when the plugin infrastructure is built (T-259), this skill should ship as part of the core plugin. Currently ships as a project-level skill in the starter kit.

## Surfaced During Build

- Q5 menu ("what do you want to tackle first?") needs validation across 3+ real onboardings. The options may not match what people actually say.
- "Project" vs "client" language tested in elicitation but the folder still lives under `clients/`. Consider renaming to `projects/` system-wide if the language shift sticks. That's a big rename — defer until there's real confusion.
