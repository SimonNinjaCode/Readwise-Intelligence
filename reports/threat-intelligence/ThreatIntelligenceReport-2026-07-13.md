# Threat Intelligence Report — 2026-07-13

## Executive Summary
Current relevant reporting is concentrated on credential and token theft, software supply-chain compromise, mailbox exfiltration tradecraft, and destructive follow-on access in hybrid Microsoft environments. The most urgent risk is identity compromise through developer and endpoint exposure, because recent supply-chain and infostealer activity can pivot into Entra ID, Azure, and Microsoft 365 with valid tokens, cookies, and credentials. The tagged Readwise collection is stale: the combined `later` and `feed` pool is dominated by older or off-scope material, so this report is based on the small subset of fresh Microsoft-relevant sources.

## Key Threats

### Miasma supply-chain campaigns targeting cloud and developer identities
**Type:** software supply-chain compromise / credential theft  
**Severity:** Critical  
**MITRE ATT&CK:** T1195.001, T1528, T1552  
**CVEs:** None cited  
**Affected:** npm ecosystems, GitHub OIDC workflows, CI/CD runners, developer workstations, Azure-connected build environments  
**M365/Azure relevance:** The malware targets Azure credentials, OIDC tokens, and cloud identities that can be used to access Azure resources, service principals, and downstream enterprise workloads.  
**Summary:** Fresh June reporting shows the Miasma malware family was used in multiple package-ecosystem compromises. In the Mastra incident, poisoned packages executed a postinstall payload that disabled TLS validation, pulled second-stage code, established persistence, and harvested host, browser, wallet, and cloud data. Separate reporting on compromised Microsoft-owned packages says the same malware family targeted AI coding agents and explicitly harvested Azure, GCP, AWS, Kubernetes, and developer-tool credentials. This is a direct cloud-identity risk, not just a package-hygiene issue.  
**Recommendations:** Rotate Azure and GitHub OIDC credentials for exposed build systems. Review CI/CD logs and developer endpoints for unexpected package lifecycle execution and outbound connections. Enforce package pinning and use `--ignore-scripts` where feasible for high-risk installs.  
**Source:** [From package to postinstall payload: Inside the Mastra npm supply chain compromise](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/); [For the 2nd time in weeks, Microsoft packages laced with credential stealer](https://arstechnica.com/security/2026/06/for-the-2nd-time-in-weeks-microsoft-packages-laced-with-credential-stealer/)

### StealC and Amadey turning endpoint theft into M365 and Entra risk
**Type:** infostealer / access-broker enablement  
**Severity:** High  
**MITRE ATT&CK:** T1555, T1539, T1059.001  
**CVEs:** None cited  
**Affected:** browsers, Outlook profiles, WinSCP, FTP/SFTP clients, personal and unmanaged endpoints  
**M365/Azure relevance:** The campaign can steal SSO tokens, session cookies, VPN credentials, and Outlook data that attackers can reuse against Microsoft 365, Entra ID, and hybrid identity paths.  
**Summary:** Microsoft’s June 24 analysis makes the enterprise impact explicit: StealC and Amadey are not just commodity stealer tools, they are feeder systems for access brokers and ransomware operators. The malware collects browser credentials and cookies, Outlook account data, and other authentication material from endpoints that may sit outside managed corporate visibility. For Microsoft tenants, that creates a practical path to account takeover and MFA bypass through stolen session material.  
**Recommendations:** Prioritize credential resets and session revocation for users with unmanaged-device exposure. Harden browser, token, and cookie protections for privileged accounts. Hunt for anomalous sign-ins that follow personal-device compromise or stealer exposure.  
**Source:** [StealC and Amadey: Breaking down infostealers and the cybercrime services that deliver them](https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/)

### Exchange Online mailbox exfiltration via hidden folder staging
**Type:** mailbox collection / audit evasion  
**Severity:** High  
**MITRE ATT&CK:** T1114.001  
**CVEs:** None  
**Affected:** Exchange Online mailboxes  
**M365/Azure relevance:** This is a native Microsoft 365 mail-theft technique that previously left little or no mailbox audit visibility.  
**Summary:** Microsoft added a new `CopyFromIPM` Exchange Online audit signal to expose a known evasion technique: copying email from the visible IPM subtree into hidden non-IPM folders and then accessing or exfiltrating it from there. The significance is not the new feature itself, but the fact that Microsoft has observed this tradecraft in real investigations. Tenants that are not querying for the new signal will miss a useful indicator of mailbox staging and possible BEC preparation.  
**Recommendations:** Add `CopyFromIPM` searches to Unified Audit Log monitoring immediately. Investigate users or mailboxes with new `MailItemsAccessed` events tied to hidden-folder copy behavior. Review mailbox compromise playbooks to include non-IPM subtree abuse.  
**Source:** [New Exchange Online Mailbox Auditing Signal: Visibility into IPM to Non-IPM Copy Activity](https://techcommunity.microsoft.com/t5/microsoft-security-community/new-exchange-online-mailbox-auditing-signal-visibility-into-ipm/ba-p/4526914)

### Storm-2603 hybrid intrusion with overlapping ransomware activity
**Type:** hybrid intrusion / ransomware precursor activity  
**Severity:** Critical  
**MITRE ATT&CK:** T1190, T1572, T1136, T1574.002  
**CVEs:** Not specified in the selected source  
**Affected:** on-premises SharePoint, Active Directory, hybrid environments, administrative tooling  
**M365/Azure relevance:** The case shows how compromise of Microsoft on-premises platforms and identity infrastructure can support persistence, privileged account creation, and cloud-adjacent incident expansion.  
**Summary:** Microsoft incident responders describe a June case where Storm-2603 targeted on-premises SharePoint, then used legitimate tools such as Velociraptor, Cloudflare tunnels, Zoho Assist, and VS Code SSH to maintain access and map the environment. Investigators also found a second actor operating in parallel with DLL sideloading and custom backdoors. For Microsoft estates, the lesson is that hybrid intrusions can quickly blend SharePoint exploitation, identity escalation, trusted tooling, and ransomware preparation into one noisy but hard-to-untangle incident.  
**Recommendations:** Patch and isolate internet-facing SharePoint aggressively. Restrict and monitor remote admin, tunneling, and support tools. Audit recent local and domain admin creation, especially when tied to SharePoint or unusual remote access activity.  
**Source:** [One intrusion, two cyberattackers: Uncovering parallel threat activity](https://www.microsoft.com/en-us/security/blog/2026/06/22/one-intrusion-two-cyberattackers-uncovering-parallel-threat-activity/)

### GigaWiper’s backdoor-plus-wiper model raises destructive-risk stakes
**Type:** destructive malware / ransomware-like wiping  
**Severity:** Critical  
**MITRE ATT&CK:** T1485, T1053.005, T1070.001  
**CVEs:** None  
**Affected:** Windows endpoints, administrative hosts, enterprise environments with exposed lateral movement paths  
**M365/Azure relevance:** While endpoint-focused, this malware fits the destructive follow-on phase that can hit hybrid identity and cloud-admin estates once attackers gain a foothold.  
**Summary:** Microsoft’s July 9 analysis describes GigaWiper as a modular Golang backdoor that consolidates disk wiping, fake ransomware, persistence, remote control, registry operations, and event-log clearing into one implant. The important point for Microsoft-centric environments is the operational flexibility: attackers can keep quiet access, then pivot to destructive impact on demand. In a tenant with synced identities or cloud-admin workstations, that kind of endpoint destruction can disrupt both response and business continuity.  
**Recommendations:** Enable tamper protection and EDR block mode broadly. Prioritize backup validation and recovery testing for privileged Windows systems. Investigate systems showing scheduled-task persistence, log clearing, or sudden destructive behavior tied to remote access activity.  
**Source:** [GigaWiper: Anatomy of a destructive backdoor assembled from multiple malware](https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/)

### AI-branded browser extension abuse creates a low-friction identity exposure path
**Type:** browser extension abuse / social engineering  
**Severity:** Medium  
**MITRE ATT&CK:** T1176, T1056  
**CVEs:** None  
**Affected:** Chromium-based browsers and users installing untrusted extensions  
**M365/Azure relevance:** Search interception and keystroke-level query capture can expose tenant administration activity, sensitive searches, and user behavior that supports later phishing or account-targeting campaigns.  
**Summary:** Microsoft documented a malicious Chromium extension impersonating Perplexity AI that forced itself as the default search provider, routed search traffic and typed suggestions through attacker-controlled infrastructure, and used browser-native request controls to hide the interception. There is no direct credential theft in the write-up, but the model matters because enterprise users often search for internal admin procedures, login flows, and troubleshooting steps from the same browser session they use for Microsoft 365 and Azure administration.  
**Recommendations:** Restrict extension installation through enterprise policy. Review browser telemetry for unauthorized search-provider changes and traffic to unapproved intermediary domains. Add extension inventory checks for privileged and helpdesk users.  
**Source:** [Chromium extension uses AI‑related branding to redirect browser search](https://www.microsoft.com/en-us/security/blog/2026/06/29/chromium-extension-uses-airelated-branding-redirect-browser-search/)

## Threat Actor Activity
Named activity in the current source set is centered on TeamPCP, Storm-2603, and ShinyHunters. TeamPCP-linked Miasma activity is targeting software supply chains and cloud-linked developer credentials, including Azure-related identity material. Storm-2603 shows continued interest in Microsoft-heavy hybrid environments through SharePoint-led intrusion paths and trusted remote tooling. ShinyHunters remains relevant because recent reporting ties the group to both SaaS token abuse and large-scale extortion activity, reinforcing that valid identities and application trust remain preferred access paths.

## Recommended Actions
1. Rotate and reissue credentials, tokens, and federated identities used by exposed CI/CD runners, developer workstations, and privileged cloud tooling.
2. Add explicit detections for Exchange Online `CopyFromIPM`, unusual mailbox access staging, and post-stealer session reuse against Microsoft 365 and Entra ID.
3. Restrict browser extensions, script interpreters, and package postinstall execution on privileged endpoints and developer systems.
4. Review SharePoint, VPN, and hybrid admin surfaces for recent exploitation, suspicious remote tooling, and unauthorized admin-account creation.
5. Tighten session controls for privileged accounts: phishing-resistant MFA, conditional access, token protection where supported, and rapid session revocation during incident response.

## Sources
- [GigaWiper: Anatomy of a destructive backdoor assembled from multiple malware](https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/)
- [From package to postinstall payload: Inside the Mastra npm supply chain compromise](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/)
- [For the 2nd time in weeks, Microsoft packages laced with credential stealer](https://arstechnica.com/security/2026/06/for-the-2nd-time-in-weeks-microsoft-packages-laced-with-credential-stealer/)
- [StealC and Amadey: Breaking down infostealers and the cybercrime services that deliver them](https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/)
- [New Exchange Online Mailbox Auditing Signal: Visibility into IPM to Non-IPM Copy Activity](https://techcommunity.microsoft.com/t5/microsoft-security-community/new-exchange-online-mailbox-auditing-signal-visibility-into-ipm/ba-p/4526914)
- [One intrusion, two cyberattackers: Uncovering parallel threat activity](https://www.microsoft.com/en-us/security/blog/2026/06/22/one-intrusion-two-cyberattackers-uncovering-parallel-threat-activity/)
- [Chromium extension uses AI‑related branding to redirect browser search](https://www.microsoft.com/en-us/security/blog/2026/06/29/chromium-extension-uses-airelated-branding-redirect-browser-search/)
