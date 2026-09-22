# Threat Intelligence Report — 2026-07-27

## Executive Summary
The most important Microsoft 365 and Entra ID risks in the current Readwise corpus remain device code phishing, AiTM-driven token theft, OAuth abuse, and ransomware operators pivoting from on-premises identity to cloud control. The most critical threat is large-scale device code phishing tied to Railway-hosted and AI-assisted infrastructure because it bypasses normal user expectations, yields valid tokens, and survives simple password resets.

The underlying `threat intelligence` collection is stale for this use case: after building the full `later` + `feed` pool and ranking the latest 20 tagged items, only a minority were directly relevant to Microsoft 365, Entra ID, AiTM, BEC, or cloud ransomware. This report therefore focuses on the subset of tagged material that materially affects Microsoft identity and cloud environments.

## Key Threats

### AI-enabled device code phishing with dynamic code generation
**Type:** Identity compromise and token theft
**Severity:** Critical
**MITRE ATT&CK:** T1566.002, T1528, T1078, T1114.001
**CVEs:** None
**Affected:** Microsoft Entra ID, Microsoft 365, Microsoft Graph, Exchange Online
**M365/Azure relevance:** Attackers abuse the legitimate device code flow to obtain valid Microsoft access and refresh tokens, then use Graph and Exchange for reconnaissance, exfiltration, and persistence.
**Summary:** Microsoft reported a widespread campaign that used dynamic device code generation, Railway-hosted infrastructure, and AI-personalized lures to improve conversion rates and scale. Post-compromise activity included Graph reconnaissance, inbox-rule persistence, email theft, and in some cases device registration for longer-lived access.
**Recommendations:** Block device code flow where it is not required. Revoke refresh tokens and force reauthentication for suspected victims. Monitor for suspicious device code sign-ins, Graph enumeration, and inbox-rule creation.
**Source:** Inside an AI-enabled device code phishing campaign — https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/

### SharePoint-delivered AiTM phishing leading to BEC
**Type:** AiTM phishing and business email compromise
**Severity:** Critical
**MITRE ATT&CK:** T1566.002, T1078, T1114.003
**CVEs:** None
**Affected:** Microsoft 365, SharePoint Online, Exchange Online, Microsoft Entra ID
**M365/Azure relevance:** The campaign abused SharePoint file-sharing workflows, stole authenticated sessions, created inbox rules, and expanded through internal and external phishing from compromised Microsoft 365 accounts.
**Summary:** Microsoft uncovered a multi-stage campaign targeting energy-sector organizations that used trusted SharePoint links for lure delivery, AiTM pages for session theft, and mailbox rules to suppress user awareness. Password resets alone were not sufficient because attackers retained session cookies and mailbox persistence.
**Recommendations:** Revoke session cookies in addition to resetting passwords. Hunt for malicious inbox rules and suspicious SharePoint-linked phishing. Enforce Conditional Access and continuous access evaluation for high-risk users.
**Source:** Resurgence of a multi-stage AiTM phishing and BEC campaign abusing SharePoint — https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/

### OAuth abuse tied to ShinyHunters tradecraft
**Type:** OAuth abuse and SaaS data theft
**Severity:** High
**MITRE ATT&CK:** T1566.004, T1528, T1671, T1213.004, T1567
**CVEs:** None
**Affected:** SaaS identities, connected applications, downstream Microsoft security monitoring workflows
**M365/Azure relevance:** The tradecraft centers on trusted OAuth relationships, consent abuse, and third-party integration risk that map directly to Entra app governance, Conditional Access, and Defender for Cloud Apps monitoring.
**Summary:** Microsoft linked multiple campaigns to ShinyHunters-style tradecraft involving vishing for OAuth consent, SaaS supply chain compromise, and misuse of guest access. The core risk is not exploit code but attacker control through sanctioned app permissions and inherited trust.
**Recommendations:** Audit connected apps and guest access aggressively. Require review of high-privilege OAuth grants and third-party integrations. Use Defender for Cloud Apps and Entra governance controls to identify risky or unused applications.
**Source:** Defending SaaS-based applications against ShinyHunters OAuth abuse — https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/

### Railway-hosted Microsoft 365 token attack infrastructure
**Type:** Device code phishing infrastructure and token replay
**Severity:** High
**MITRE ATT&CK:** T1566.002, T1528, T1078
**CVEs:** None
**Affected:** Microsoft 365 identities, Entra sign-in telemetry, Exchange Online, SharePoint Online
**M365/Azure relevance:** Railway-hosted infrastructure generated or replayed Microsoft 365 tokens at scale from otherwise clean cloud IP space, reducing the value of simple reputation-based blocking.
**Summary:** Huntress documented a campaign affecting hundreds of organizations in which attackers abused Railway PaaS to host credential-harvesting and token-collection infrastructure for Microsoft 365 device code phishing. The campaign’s lure diversity and automation strongly suggest industrialized phishing operations rather than isolated manual activity.
**Recommendations:** Block or tightly control device code authentication. Monitor and, where appropriate, restrict sign-ins from known abusive cloud infrastructure ranges. Prioritize identity-layer detections over domain-based phishing controls alone.
**Source:** Riding the Rails: Threat Actors Abuse Railway.com PaaS as Microsoft 365 Token Attack Infrastructure — https://www.huntress.com/blog/railway-paas-m365-token-replay-campaign

### Hybrid-cloud ransomware pivot through Entra Connect and cloud admin abuse
**Type:** Ransomware and identity pivot from on-premises to cloud
**Severity:** Critical
**MITRE ATT&CK:** T1078, T1098, T1486
**CVEs:** CVE-2022-47966, CVE-2023-4966, CVE-2023-29300, CVE-2023-38203
**Affected:** Microsoft Entra Connect, Microsoft Entra ID, hybrid identity, on-premises AD, cloud administrative roles
**M365/Azure relevance:** Storm-0501 moved from local compromise to Entra control by targeting sync accounts and cloud admins, then created durable cloud backdoors and deployed ransomware in hybrid estates.
**Summary:** Microsoft observed Storm-0501 stealing credentials, extracting Entra Connect sync secrets, pivoting into Microsoft Entra ID, and in some cases establishing federated backdoor access before ransomware deployment. This is a clear case where hybrid identity remains the bridge between endpoint compromise and tenant-wide cloud risk.
**Recommendations:** Restrict and monitor Entra Connect sync accounts. Enforce MFA and Conditional Access for all privileged cloud identities. Investigate federation changes, new trusted domains, and unusual sync-account sign-ins immediately.
**Source:** Storm-0501: Ransomware attacks expanding to hybrid cloud environments — https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/

### File-hosting abuse for identity phishing and follow-on AiTM
**Type:** Identity phishing, token theft, and BEC enablement
**Severity:** High
**MITRE ATT&CK:** T1566.002, T1528, T1078
**CVEs:** None
**Affected:** SharePoint Online, OneDrive, Dropbox-linked workflows, Microsoft Entra ID
**M365/Azure relevance:** Attackers are abusing normal file-sharing workflows in SharePoint and OneDrive to force reauthentication, hand users into AiTM pages, and expand BEC activity across Microsoft 365 tenants.
**Summary:** Microsoft described campaigns that used legitimate file-hosting notifications, restricted-access documents, and view-only files to avoid detonation and user suspicion. The user ultimately landed on AiTM infrastructure after interacting with what looked like standard collaboration workflows.
**Recommendations:** Hunt for suspicious secure-link sharing patterns and unusual notification-driven sign-ins. Apply risk-based Conditional Access and phishing-resistant authentication. Review vendor allow lists that may over-trust collaboration senders.
**Source:** File hosting services misused for identity phishing — https://www.microsoft.com/en-us/security/blog/2024/10/08/file-hosting-services-misused-for-identity-phishing/

## Threat Actor Activity
Storm-2372 remains the most relevant named actor for Microsoft identity abuse in this corpus because it operationalized device code phishing against governments, NGOs, and enterprise targets and then used Microsoft Graph for collection and internal expansion. Microsoft’s April 2026 reporting shows the same tradecraft evolving into more automated, AI-assisted infrastructure associated with EvilTokens-style operations.

ShinyHunters-linked activity stands out for OAuth abuse against SaaS ecosystems, with emphasis on consent abuse, trusted integrations, and persistent API-level access rather than endpoint malware. Storm-0501 remains the key hybrid-cloud ransomware actor in the collection because it demonstrates how on-premises credential theft and Entra Connect compromise can produce tenant-level cloud persistence and later ransomware impact.

## Recommended Actions
1. Block device code flow for all users and apps that do not require it, then review exceptions quarterly.
2. Require phishing-resistant authentication for privileged users and high-impact apps, especially Exchange Online, SharePoint Online, and Microsoft Graph access paths.
3. Treat suspected AiTM compromise as token theft, not just password theft: revoke refresh tokens, invalidate sessions, remove inbox rules, and review MFA changes.
4. Audit OAuth consent, connected apps, guest access, and high-privilege service principals in Entra and downstream SaaS integrations.
5. Lock down Microsoft Entra Connect and monitor sync-account sign-ins, federation changes, new domains, and unusual Graph activity from administrative identities.
6. Expand detection for Graph reconnaissance, mailbox access anomalies, file-sharing abuse, and cloud sign-ins from ephemeral infrastructure providers.
7. Retag or prune the Readwise `threat intelligence` collection so current Microsoft identity and cloud threats are not buried under unrelated security news.

## Sources
- Inside an AI-enabled device code phishing campaign — https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/
- Resurgence of a multi-stage AiTM phishing and BEC campaign abusing SharePoint — https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/
- Defending SaaS-based applications against ShinyHunters OAuth abuse — https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/
- Riding the Rails: Threat Actors Abuse Railway.com PaaS as Microsoft 365 Token Attack Infrastructure — https://www.huntress.com/blog/railway-paas-m365-token-replay-campaign
- Storm-0501: Ransomware attacks expanding to hybrid cloud environments — https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/
- File hosting services misused for identity phishing — https://www.microsoft.com/en-us/security/blog/2024/10/08/file-hosting-services-misused-for-identity-phishing/
- Storm-2372 conducts device code phishing campaign — https://www.microsoft.com/en-us/security/blog/2025/02/13/storm-2372-conducts-device-code-phishing-campaign/
- Investigating OAuth App Abuse with the Graph Activity Log — https://practical365.com/investigating-oauth-app-abuse-with-the-graph-activity-log/
