# Threat Intelligence Report — 2026-06-15

## Executive Summary
Trusted software supply chains and developer identity paths remain the dominant risk for Microsoft 365 and Azure-adjacent environments. The most serious current issue is the repeated compromise of trusted publisher workflows to steal Azure and OIDC credentials, while phishing and AiTM activity continues to target Microsoft sign-in flows and Exchange Online data. The current Microsoft-focused signal is coming from recent saved items, but the broader `threat intelligence` tag set is still weighed down by stale older material and should be refreshed.

## Key Threats

### Hidden-folder Exchange Online mailbox exfiltration
**Type:** post-compromise email data theft and audit evasion
**Severity:** High
**MITRE ATT&CK:** T1114.001, T1020, T1564
**CVEs:** None
**Affected:** Exchange Online mailboxes
**M365/Azure relevance:** Directly affects Exchange Online investigations and detection coverage for mailbox exfiltration.
**Summary:** Microsoft added a new `CopyFromIPM` audit signal after investigations found actors copying mail from visible mailbox folders into the hidden non-IPM subtree before exfiltrating it. The technique matters because it previously created a blind spot in mailbox auditing and can hide data staging inside a compromised tenant.
**Recommendations:** Query the Unified Audit Log for `CopyFromIPM`; review high-risk mailbox access and delegated permissions; alert on hidden-folder copy activity followed by unusual mailbox access or export.
**Source:** [New Exchange Online Mailbox Auditing Signal: Visibility into IPM to Non-IPM Copy Activity](https://techcommunity.microsoft.com/t5/microsoft-security-community/new-exchange-online-mailbox-auditing-signal-visibility-into-ipm/ba-p/4526914)

### AI-branded phishing and AiTM against Microsoft sign-in flows
**Type:** phishing, AiTM, token theft
**Severity:** High
**MITRE ATT&CK:** T1566.001, T1566.002, T1557, T1528
**CVEs:** None
**Affected:** Microsoft 365 user accounts, browsers, endpoints
**M365/Azure relevance:** Microsoft observed a Claude-branded campaign that likely ended at a Microsoft sign-in page to steal credentials and session material, making this directly relevant to Entra ID and M365 session security.
**Summary:** Recent campaigns used ChatGPT, Claude, DeepSeek, and Copilot branding to drive phishing, malvertising, and malware delivery. Microsoft linked the broader activity to Storm-3075 and observed infrastructure overlap with Fox Tempest-signed malware, with the Claude-themed chain specifically aligning to AiTM-style token interception against Microsoft identities.
**Recommendations:** Enforce phishing-resistant MFA for privileged and high-risk users; enable Safe Links, Zero-hour Auto Purge, and network protection; hunt for unfamiliar session properties, anomalous token activity, and suspicious sign-ins following branded lure emails.
**Source:** [AI brands as bait: How threat actors are using the AI hype in social engineering](https://www.microsoft.com/en-us/security/blog/2026/06/08/ai-brands-as-bait-how-threat-actors-are-using-the-ai-hype-in-social-engineering/)

### Miasma compromise of Microsoft publisher workflows
**Type:** software supply-chain compromise and cloud credential theft
**Severity:** Critical
**MITRE ATT&CK:** T1195.001, T1528, T1552.001
**CVEs:** None
**Affected:** Microsoft-hosted packages, developer workstations, CI/CD runners, Azure identities
**M365/Azure relevance:** The malware explicitly harvested Azure identities and legitimate OIDC publishing tokens, creating a direct path from developer compromise into cloud control planes.
**Summary:** Seventy-three Microsoft packages were found carrying credential-stealing code tied to the Miasma worm, the second compromise involving the same Microsoft publishing account in weeks. The malware targeted Azure, AWS, GCP, Kubernetes, password managers, and developer tooling, while using legitimate identity and provenance workflows to blend into normal release activity.
**Recommendations:** Rotate developer, CI/CD, and cloud credentials exposed during the window; review GitHub OIDC token issuance and provenance events for anomalies; investigate any developer machine or AI coding agent that opened affected packages.
**Source:** [For the 2nd time in weeks, Microsoft packages laced with credential stealer](https://arstechnica.com/security/2026/06/for-the-2nd-time-in-weeks-microsoft-packages-laced-with-credential-stealer/)

### Red Hat npm Miasma campaign stealing cloud and pipeline secrets
**Type:** software supply-chain compromise
**Severity:** Critical
**MITRE ATT&CK:** T1195.001, T1528, T1552.001
**CVEs:** None
**Affected:** npm consumers, GitHub Actions, Azure, AWS, GCP, HashiCorp Vault, Kubernetes
**M365/Azure relevance:** The payload harvested Azure IMDS tokens and cloud credentials from build systems, making it relevant to Azure-connected engineering environments.
**Summary:** Trojanized `@redhat-cloud-services` packages abused a trusted GitHub Actions OIDC publishing path and carried valid provenance while stealing secrets from developer systems and CI/CD runners. The malware collected Azure, GitHub, npm, and other cloud credentials, then attempted to propagate through compromised maintainer access.
**Recommendations:** Identify direct and transitive exposure to affected package versions; rotate Azure, GitHub, npm, and CI/CD secrets; restrict lifecycle script execution and enforce private-scope registry controls.
**Source:** [Preinstall to persistence: Inside the Red Hat npm Miasma credential-stealing campaign](https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/)

### Dependency confusion campaign profiling enterprise developer environments
**Type:** dependency confusion and pre-positioning for follow-on compromise
**Severity:** High
**MITRE ATT&CK:** T1195.001, T1082, T1592
**CVEs:** None
**Affected:** enterprise npm ecosystems, developer endpoints, internal package consumers
**M365/Azure relevance:** This is a realistic path into Azure-connected build systems and developer identities even when the initial payload is only reconnaissance.
**Summary:** Microsoft identified packages that mimicked internal corporate namespaces and used install-time execution to map hostnames, environment variables, project roots, and developer context. The actor kept the payload in reconnaissance mode but built in a clear path to enable full exploitation later, which is a strong warning for organizations relying on private package naming conventions without strict registry controls.
**Recommendations:** Scope-lock internal package namespaces to private registries; pin known-good internal dependencies; alert on outbound npm-install traffic to `oob.moika[.]tech` and detached child processes spawned during package installation.
**Source:** [Malicious npm packages abuse dependency confusion to profile developer environments](https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/)

### Typosquatted npm packages stealing cloud and CI/CD secrets
**Type:** typosquatting and supply-chain credential theft
**Severity:** High
**MITRE ATT&CK:** T1195.001, T1528, T1552.001
**CVEs:** None
**Affected:** OpenSearch and Elastic-adjacent package consumers, AWS, Vault, GitHub Actions, npm tokens
**M365/Azure relevance:** The tradecraft maps cleanly to Azure-connected build environments even though the observed payload emphasized AWS and Vault; the broader lesson is developer-to-cloud credential theft through install-time package execution.
**Summary:** A single actor published 14 malicious packages that used npm lifecycle hooks, Bun runtime downloads, and detached payload execution to harvest cloud and CI/CD secrets. The campaign was designed for silent credential theft and downstream supply-chain pivoting rather than immediate disruptive impact.
**Recommendations:** Disable or tightly control install scripts; rotate pipeline and package-publishing tokens; alert on Bun runtime downloads, metadata-service access, and unusual build-host egress during package installation.
**Source:** [Typosquatted npm packages used to steal cloud and CI/CD secrets](https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/)

### Azure-hosted edge appliance compromise leading to identity abuse
**Type:** edge exploitation, lateral movement, identity attack
**Severity:** Critical
**MITRE ATT&CK:** T1190, T1021.004, T1187, T1557
**CVEs:** CVE-2025-53521, CVE-2025-33073
**Affected:** Azure-hosted F5 BIG-IP VE, Confluence, Active Directory and hybrid identity infrastructure
**M365/Azure relevance:** The initial foothold was an Azure-hosted F5 appliance, and the intrusion progressed toward identity compromise, showing how Azure edge assets can become the first step in broader tenant-impacting attacks.
**Summary:** Microsoft documented an intrusion that began on an end-of-life Azure-hosted F5 BIG-IP instance, pivoted into Linux and Confluence systems, and then moved toward credential theft and Kerberos relay activity against directory infrastructure. The case is important because it shows hybrid-cloud compromise crossing from network edge to application tier to identity plane without needing a direct M365 exploit.
**Recommendations:** Treat internet-facing appliances as Tier 0 assets; patch internal apps with the same urgency as exposed services; harden NTLM, SMB, LDAP, and privileged service accounts; monitor for SSH logons and unusual admin activity originating from edge appliances.
**Source:** [From edge appliance to enterprise compromise: Multi-stage Linux intrusion via F5 and Confluence](https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/)

## Threat Actor Activity
Storm-3075 continued to use branded lures and malicious download infrastructure, including AI-themed social engineering that overlaps with Microsoft identity risk. Fox Tempest remained relevant as a malware-signing service that increased trust in payload delivery. TeamPCP-linked Miasma and Shai-Hulud tradecraft continued to show up in trusted software ecosystems, with repeated emphasis on GitHub, npm, OIDC, CI/CD, and cloud credential theft. Microsoft also tied one dependency-confusion cluster to a single operator spanning multiple npm personas, while the edge-to-identity intrusion chain showed continued pressure on F5 and internal application paths that can lead to directory compromise.

## Recommended Actions
- Hunt immediately for Azure, GitHub, npm, and CI/CD credential exposure tied to recent package installs, especially OIDC token use and unusual publish activity.
- Add detections for Exchange Online `CopyFromIPM`, AiTM-style session anomalies, unfamiliar session cookies, and mailbox access that follows suspicious sign-in chains.
- Enforce phishing-resistant MFA and tighter Conditional Access for privileged users, administrators, and developer identities with cloud or package publishing rights.
- Scope-lock private package namespaces, disable unnecessary npm lifecycle scripts, and monitor for Bun downloads or install-time child processes on developer and build hosts.
- Treat internet-facing appliances and internal SaaS applications as identity-critical assets: patch quickly, retire end-of-life systems, and harden relay-prone authentication paths.
- Refresh the `threat intelligence` tagging set so current Microsoft 365 and Azure material is not buried under stale older feed content.

## Sources
- [New Exchange Online Mailbox Auditing Signal: Visibility into IPM to Non-IPM Copy Activity](https://techcommunity.microsoft.com/t5/microsoft-security-community/new-exchange-online-mailbox-auditing-signal-visibility-into-ipm/ba-p/4526914)
- [AI brands as bait: How threat actors are using the AI hype in social engineering](https://www.microsoft.com/en-us/security/blog/2026/06/08/ai-brands-as-bait-how-threat-actors-are-using-the-ai-hype-in-social-engineering/)
- [For the 2nd time in weeks, Microsoft packages laced with credential stealer](https://arstechnica.com/security/2026/06/for-the-2nd-time-in-weeks-microsoft-packages-laced-with-credential-stealer/)
- [Preinstall to persistence: Inside the Red Hat npm Miasma credential-stealing campaign](https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/)
- [Malicious npm packages abuse dependency confusion to profile developer environments](https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/)
- [Typosquatted npm packages used to steal cloud and CI/CD secrets](https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/)
- [From edge appliance to enterprise compromise: Multi-stage Linux intrusion via F5 and Confluence](https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/)
