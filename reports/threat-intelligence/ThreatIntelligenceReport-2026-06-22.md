# Threat Intelligence Report — 2026-06-22

## Executive Summary
Current Microsoft 365 and identity-relevant reporting is centered on token theft, adversary-in-the-middle (AiTM) phishing, and cloud credential theft through software supply chains. The most urgent risk is large-scale device code phishing against Entra ID and Microsoft 365, because it converts normal user MFA into valid attacker tokens and enables immediate mailbox abuse and Graph reconnaissance. The Reader tag set is stale overall: the full `later` + `feed` pool was dominated by older material, but the latest 20 selected items still produced a usable current set from 2026-04-06 through 2026-06-18.

## Key Threats

### AI-enabled device code phishing against Entra ID
**Type:** phishing and token theft
**Severity:** Critical
**MITRE ATT&CK:** T1566.002, T1078, T1114.001
**CVEs:** None
**Affected:** Microsoft Entra ID, Microsoft 365, Exchange Online, Microsoft Graph
**M365/Azure relevance:** The campaign abuses the legitimate device code flow to obtain valid Microsoft access and refresh tokens, then uses those tokens for mailbox access, inbox-rule persistence, device registration, and Graph reconnaissance.
**Summary:** Microsoft described a widespread campaign that automated live device-code generation, used cloud-hosted redirect infrastructure, and focused follow-on activity on financial and executive users. The attack flow reduced code-expiry friction, copied device codes to victims’ clipboards, and led to email exfiltration and persistence through malicious inbox rules.
**Recommendations:** Block device code flow where it is not required. Enforce phishing-resistant MFA and Conditional Access for privileged and high-risk users. Hunt for device-code sign-ins followed by new inbox rules, suspicious device registration, or unusual Microsoft Graph access.
**Source:** Inside an AI-enabled device code phishing campaign - https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/

### Forest Blizzard DNS hijacking supporting Outlook on the web AiTM
**Type:** AiTM and credential interception
**Severity:** Critical
**MITRE ATT&CK:** T1557, T1584, T1078
**CVEs:** None
**Affected:** Outlook on the web users, remote workers on unmanaged SOHO routers, identity sessions protected only by warning-dependent TLS trust
**M365/Azure relevance:** Microsoft observed follow-on TLS AiTM activity against Microsoft Outlook on the web domains after router compromise and malicious DNS reconfiguration.
**Summary:** Forest Blizzard and Storm-2754 compromised vulnerable SOHO routers, redirected DNS traffic to actor-controlled resolvers, and selectively forced victims toward malicious infrastructure. Microsoft assessed that the actor used this position to intercept cloud traffic, including Outlook on the web sessions, with potential for wider-scale AiTM against remote and hybrid users.
**Recommendations:** Treat unmanaged home and small-office routers as part of the identity attack surface. Enforce Zero Trust DNS or equivalent trusted DNS controls on endpoints. Require phishing-resistant MFA, sign-in risk policies, and review risky sign-ins tied to remote or home-user populations.
**Source:** SOHO router compromise leads to DNS hijacking and adversary-in-the-middle attacks - https://www.microsoft.com/en-us/security/blog/2026/04/07/soho-router-compromise-leads-to-dns-hijacking-and-adversary-in-the-middle-attacks/

### AI-brand phishing and Claude-themed AiTM lures
**Type:** phishing, malvertising, and token theft
**Severity:** High
**MITRE ATT&CK:** T1566.002, T1204.001, T1557
**CVEs:** None
**Affected:** Microsoft 365 users, Entra ID identities, browser sessions, endpoints exposed to GitHub-hosted lure payloads
**M365/Azure relevance:** The Claude-themed branch of the campaign used attacker infrastructure that Microsoft linked to a likely final Microsoft sign-in stage consistent with AiTM token theft. Microsoft also documented post-compromise detections such as anomalous tokens and unfamiliar session-cookie sign-ins.
**Summary:** Threat actors used ChatGPT, Claude, DeepSeek, and Copilot branding to improve click-through rates across phishing and malvertising campaigns. The highest-priority branch for Microsoft environments used Claude policy-appeal lures, CAPTCHA gating, redirect logic, and likely Microsoft sign-in interception to steal tokens; other branches delivered Vidar and similar stealers from GitHub-hosted payloads.
**Recommendations:** Tighten Defender for Office 365 Safe Links and anti-phishing policies. Review Entra ID Protection alerts for anomalous token and unfamiliar sign-in properties. Train users that AI brand familiarity does not validate the sign-in flow or attachment.
**Source:** AI brands as bait: How threat actors are using the AI hype in social engineering - https://www.microsoft.com/en-us/security/blog/2026/06/08/ai-brands-as-bait-how-threat-actors-are-using-the-ai-hype-in-social-engineering/

### Supply-chain malware stealing Azure, OIDC, and developer credentials
**Type:** software supply-chain compromise
**Severity:** High
**MITRE ATT&CK:** T1195.001, T1552, T1528
**CVEs:** None
**Affected:** Developer workstations, CI/CD runners, GitHub Actions, npm publishing pipelines, Azure identities and metadata endpoints
**M365/Azure relevance:** Multiple campaigns targeted Azure tokens, OIDC trust paths, and cloud credentials that can be used to pivot from build systems into Azure subscriptions, Entra-backed applications, and Microsoft-owned package ecosystems.
**Summary:** Recent package compromises across Red Hat, Mastra, and Microsoft-linked ecosystems show a clear pattern: threat actors are abusing trusted publisher workflows to run install-time malware that steals GitHub, npm, AWS, GCP, and Azure credentials, then republishs malware with apparently legitimate provenance. Microsoft’s own package incidents showed repeated abuse of OIDC-backed workflows and token theft focused on cloud identities.
**Recommendations:** Run installs with `--ignore-scripts` in sensitive build paths where feasible. Rotate Azure, Entra app, GitHub, and CI/CD credentials after any exposure to affected packages. Audit build logs for unusual metadata endpoint access, outbound connections, and unexpected package republishing.
**Source:** Preinstall to persistence: Inside the Red Hat npm Miasma credential-stealing campaign - https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/; From package to postinstall payload: Inside the Mastra npm supply chain compromise - https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/; For the 2nd time in weeks, Microsoft packages laced with credential stealer - https://arstechnica.com/security/2026/06/for-the-2nd-time-in-weeks-microsoft-packages-laced-with-credential-stealer/

### Dependency confusion reconnaissance targeting enterprise build environments
**Type:** supply-chain reconnaissance
**Severity:** High
**MITRE ATT&CK:** T1195.001, T1082, T1083
**CVEs:** None
**Affected:** Developer endpoints, internal package consumers, CI/CD systems, organizations with mis-scoped private package resolution
**M365/Azure relevance:** Microsoft reported package payloads that profile developer environments and can later switch from recon mode to exploitation, including collection of cloud tokens and environment data relevant to Azure-backed applications and pipelines.
**Summary:** Microsoft found 33 malicious npm packages impersonating internal enterprise scopes and abusing dependency confusion to run silent reconnaissance payloads. The current payloads focused on environment fingerprinting and developer context collection, but the architecture supports server-side activation of fuller exploitation later, including cloud credential abuse.
**Recommendations:** Scope-lock all internal package namespaces to private registries. Hunt for outbound traffic to `oob.moika[.]tech` and for suspicious `postinstall` execution under internal-looking scopes. Review lockfiles and caches for unexpected public packages with internal namespace names.
**Source:** Malicious npm packages abuse dependency confusion to profile developer environments - https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/

### Storm-1175 exploitation feeding Medusa ransomware
**Type:** ransomware intrusion
**Severity:** High
**MITRE ATT&CK:** T1190, T1021, T1003, T1486
**CVEs:** CVE-2023-21529, CVE-2024-1709, CVE-2025-31161, CVE-2026-1731
**Affected:** Web-facing servers, on-prem Exchange, hybrid identity infrastructure, backup systems, Windows domain environments
**M365/Azure relevance:** Storm-1175 has exploited Microsoft Exchange and uses credential theft, RMM tooling, and domain control to move into environments that often synchronize with Entra ID and host Microsoft 365-adjacent identity workflows.
**Summary:** Microsoft reported that Storm-1175 continues to weaponize newly disclosed vulnerabilities, sometimes within a day, to gain initial access and move rapidly toward credential theft, data exfiltration, and Medusa ransomware deployment. Exchange remains part of the actor’s historical exploit set, and the post-compromise tradecraft includes account creation, RMM persistence, LSASS theft, and security-control tampering.
**Recommendations:** Patch exposed web-facing applications quickly, especially Exchange and other internet-facing administration paths. Prioritize alerts for LSASS access, new admin creation, and RMM deployment from unusual sources. Harden hybrid identity and backup systems because they are valuable pivots during ransomware operations.
**Source:** Storm-1175 focuses gaze on vulnerable web-facing assets in high-tempo Medusa ransomware operations - https://www.microsoft.com/en-us/security/blog/2026/04/06/storm-1175-focuses-gaze-on-vulnerable-web-facing-assets-in-high-tempo-medusa-ransomware-operations/

### Exchange Online mailbox audit evasion through IPM-to-Non-IPM copy
**Type:** defense evasion and email collection
**Severity:** Medium
**MITRE ATT&CK:** T1114.001, T1564
**CVEs:** None
**Affected:** Exchange Online mailboxes
**M365/Azure relevance:** Microsoft introduced a new Exchange Online audit signal specifically because attackers have been copying visible mailbox content into hidden non-IPM areas before exfiltration.
**Summary:** Microsoft disclosed a new `MailItemsAccessed` `AccessType=CopyFromIPM` event to expose a previously weak visibility point in Exchange Online. The technique matters because attackers could stage user-facing mailbox content in hidden folders and access it there with little audit coverage.
**Recommendations:** Start querying for `CopyFromIPM` immediately in the Unified Audit Log. Add this signal to mailbox-compromise playbooks and BEC investigations. Review whether copy operations and hidden-folder access are already covered in detection engineering.
**Source:** New Exchange Online Mailbox Auditing Signal: Visibility into IPM to Non-IPM Copy Activity - https://techcommunity.microsoft.com/t5/microsoft-security-community/new-exchange-online-mailbox-auditing-signal-visibility-into-ipm/ba-p/4526914

## Threat Actor Activity
Forest Blizzard and its Storm-2754 subgroup used compromised SOHO routers for DNS hijacking and selective TLS AiTM against Outlook on the web. Storm-1175 continued high-tempo Medusa operations by exploiting vulnerable web-facing assets, including Exchange in its longer-running playbook. Microsoft linked AI-themed malvertising to Storm-3075 and malware signing support to Fox Tempest. TeamPCP-linked Shai-Hulud and Miasma activity continued to drive supply-chain compromise focused on cloud and CI/CD credentials. Microsoft also tied scaled device code phishing to the EvilToken phishing-as-a-service ecosystem.

## Recommended Actions
- Block or tightly restrict device code flow in Entra ID, and require phishing-resistant MFA for privileged and high-risk users.
- Hunt for post-authentication abuse in Microsoft 365: suspicious inbox rules, risky sign-ins, device registration, and unusual Graph or `MailItemsAccessed` activity.
- Treat developer tooling and CI/CD as identity infrastructure: rotate exposed Azure, GitHub, npm, and OIDC credentials and review package-install paths that allow script execution.
- Scope-lock private package namespaces so internal names never resolve from the public npm registry.
- Patch internet-facing applications on an accelerated cycle, with explicit coverage for Exchange, file-transfer tools, remote access tools, and other perimeter services.
- Extend protection to remote and hybrid users by enforcing trusted DNS, reviewing unmanaged router risk, and monitoring for anomalous Outlook on the web access.
- Add Exchange `CopyFromIPM` monitoring to BEC and mailbox-compromise investigations.

## Sources
- Inside an AI-enabled device code phishing campaign - https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/
- SOHO router compromise leads to DNS hijacking and adversary-in-the-middle attacks - https://www.microsoft.com/en-us/security/blog/2026/04/07/soho-router-compromise-leads-to-dns-hijacking-and-adversary-in-the-middle-attacks/
- AI brands as bait: How threat actors are using the AI hype in social engineering - https://www.microsoft.com/en-us/security/blog/2026/06/08/ai-brands-as-bait-how-threat-actors-are-using-the-ai-hype-in-social-engineering/
- Preinstall to persistence: Inside the Red Hat npm Miasma credential-stealing campaign - https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/
- From package to postinstall payload: Inside the Mastra npm supply chain compromise - https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
- For the 2nd time in weeks, Microsoft packages laced with credential stealer - https://arstechnica.com/security/2026/06/for-the-2nd-time-in-weeks-microsoft-packages-laced-with-credential-stealer/
- Malicious npm packages abuse dependency confusion to profile developer environments - https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/
- Storm-1175 focuses gaze on vulnerable web-facing assets in high-tempo Medusa ransomware operations - https://www.microsoft.com/en-us/security/blog/2026/04/06/storm-1175-focuses-gaze-on-vulnerable-web-facing-assets-in-high-tempo-medusa-ransomware-operations/
- New Exchange Online Mailbox Auditing Signal: Visibility into IPM to Non-IPM Copy Activity - https://techcommunity.microsoft.com/t5/microsoft-security-community/new-exchange-online-mailbox-auditing-signal-visibility-into-ipm/ba-p/4526914
