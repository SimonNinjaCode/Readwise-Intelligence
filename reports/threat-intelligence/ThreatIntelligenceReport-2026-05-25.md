# Threat Intelligence Report — 2026-05-25

## Executive Summary
This cycle’s most actionable items are supply-chain and infrastructure-led intrusions that end in credential theft and identity compromise: compromised packages in CI/CD, malware signing services, and edge-appliance footholds that pivot into directory attacks. The highest-risk theme for Microsoft 365 and Azure tenants is secondary access via stolen tokens/keys (GitHub Actions, cloud secrets, and admin credentials) and subsequent account takeover.

## Key Threats

### Multi-stage intrusion via edge appliance and Confluence leading to identity compromise
**Type:** Edge appliance compromise → lateral movement → identity compromise
**Severity:** High
**MITRE ATT&CK:** T1190, T1021.004, T1059.004, T1557, T1078.002
**CVEs:** N/A (campaign references exploitation of public-facing applications)
**Affected:** Azure-hosted F5 BIG-IP (VE), Linux hosts, Confluence, Active Directory/identity systems
**M365/Azure relevance:** Highlights Azure-hosted edge appliances as entry points; identity compromise enables downstream access to Microsoft services (Entra/M365/Azure) through trusted identities and harvested credentials.
**Summary:** Microsoft described an intrusion that began with compromise of an internet-facing F5 BIG-IP appliance and pivoted into internal Linux systems. The actor used network recon tooling, then leveraged a vulnerable SaaS app (Confluence) and its credentials for relay-style authentication activity against Active Directory—illustrating a multi-domain path from perimeter device to identity control.
**Recommendations:** Patch/retire end-of-life edge appliances, inventory and monitor privileged SSH/sudo identities, and prioritize detections for relay/forced-auth behavior and credential reuse after appliance compromise.
**Source:** From edge appliance to enterprise compromise: Multi-stage Linux intrusion via F5 and Confluence — https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/

### CI/CD supply-chain attack stealing GitHub Actions and cloud secrets (Mini Shai Hulud / @antv npm compromise)
**Type:** Software supply chain → credential theft
**Severity:** Critical
**MITRE ATT&CK:** T1195, T1555, T1059.007, T1105
**CVEs:** N/A
**Affected:** npm ecosystem, GitHub Actions runners, downstream apps and build pipelines
**M365/Azure relevance:** Stolen CI/CD secrets frequently include Azure credentials, GitHub tokens, and vault/Kubernetes secrets that can be used for cloud footholds and identity abuse.
**Summary:** Microsoft reported a compromise of an @antv maintainer account leading to malicious npm package releases that execute during install and target Linux GitHub Actions environments. The payload is designed to extract GitHub tokens and secrets and to enumerate/steal credentials across common cloud and secret stores (including AWS and Vault) with techniques like runner process memory scraping.
**Recommendations:** Identify and purge compromised package versions, rotate CI/CD tokens and any downstream secrets, and hunt for suspicious `node`/`npm` network activity and package-install execution on runners.
**Source:** Mini Shai Hulud: Compromised @antv npm packages enable CI/CD credential theft — https://www.microsoft.com/en-us/security/blog/2026/05/20/mini-shai-hulud-compromised-antv-npm-packages-enable-ci-cd-credential-theft/

### Malware-signing-as-a-service abusing Microsoft Artifact Signing (Fox Tempest)
**Type:** Initial access enablement / defense evasion service
**Severity:** High
**MITRE ATT&CK:** T1588.003, T1588.002, T1553.002
**CVEs:** N/A
**Affected:** Malware distribution chains, short-lived fraudulent code-signing certificates, Azure tenants/subscriptions
**M365/Azure relevance:** Abuse of Microsoft signing infrastructure and Azure tenant sprawl increases the success rate of malware delivery that can lead to credential theft, BEC, and ransomware in M365/Azure environments.
**Summary:** Microsoft detailed a malware-signing service that generated short-lived certificates via Artifact Signing to make malware appear trusted. The operation supported broader cybercrime activity (including ransomware ecosystems) and was backed by large-scale creation of Azure tenants/subscriptions and high-volume certificate issuance.
**Recommendations:** Monitor for signed-but-suspicious binaries, tighten application control policies, and review telemetry for anomalous certificate/signing and Azure tenant activity tied to untrusted software delivery.
**Source:** Exposing Fox Tempest: A malware-signing service operation — https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/

### Linux privilege escalation used for post-compromise expansion in cloud and hybrid estates (CopyFail, Dirty Frag)
**Type:** Post-compromise privilege escalation
**Severity:** High
**MITRE ATT&CK:** T1068
**CVEs:** CVE-2026-31431, CVE-2026-43284, CVE-2026-43500
**Affected:** Linux hosts (including container/CI runner and Kubernetes-adjacent environments)
**M365/Azure relevance:** Linux fleets often host identity-adjacent services (connectors, CI, gateways) and cloud workloads; reliable local privilege escalation accelerates ransomware staging and credential access.
**Summary:** Reporting highlights active exploitation/testing of Linux kernel privilege escalation paths. CopyFail (CVE-2026-31431) is treated as KEV-listed with public PoCs, and Dirty Frag is positioned as a newer, more reliable escalation path across common enterprise Linux distributions. Both materially increase the impact of any initial foothold (SSH, web shell, container breakout).
**Recommendations:** Patch and reboot affected kernels, prioritize remediation on CI runners and Kubernetes nodes, and increase monitoring for abnormal privilege escalation and kernel-module usage on Linux.
**Source:** "Copy Fail" Lands on CISA's KEV: A Nine-Year-Old Linux Bug Becomes a Patch Deadline — https://darkwebinformer.com/copy-fail-lands-on-cisas-kev-a-nine-year-old-linux-bug-becomes-a-patch-deadline/

### Prompt injection to host-level execution in AI agent frameworks (Semantic Kernel)
**Type:** Application/framework vulnerability enabling RCE via tool/plugin invocation
**Severity:** High
**MITRE ATT&CK:** T1204, T1059, T1105
**CVEs:** CVE-2026-25592, CVE-2026-26030
**Affected:** Semantic Kernel-based agents; tool/plugin invocation paths
**M365/Azure relevance:** Organizations building agents around Microsoft stacks (including Azure-hosted AI apps) risk turning prompt injection into execution and data access against connected systems.
**Summary:** Microsoft reported two critical issues in Semantic Kernel where prompt injection combined with specific configurations could be leveraged to reach code-execution primitives. The writeup underscores that once agents are wired to tools, model-controlled parameters must be treated as attacker-controlled input.
**Recommendations:** Patch affected Semantic Kernel versions, review agent tool/plugin exposure, and add monitoring for suspicious child processes and command execution originating from agent hosts.
**Source:** When prompts become shells: RCE vulnerabilities in AI agent frameworks — https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/

### Cascading developer-tool supply-chain compromises and token theft (TeamPCP / GitHub-linked VS Code extension)
**Type:** Software supply chain → credential and token theft
**Severity:** High
**MITRE ATT&CK:** T1195, T1555, T1078
**CVEs:** N/A
**Affected:** Developer workstations, VS Code extensions, source repositories, long-lived tokens/credentials
**M365/Azure relevance:** Stolen developer tokens often include Azure/GitHub credentials; compromises can lead to access to build systems, cloud resources, and SaaS identities used for Microsoft services.
**Summary:** Reporting describes a cycle of supply-chain compromises targeting developer tools and extensions, with follow-on credential theft used to publish additional malicious artifacts and expand access. The operational pattern is consistent with rapid lateral spread through static credentials and personal access tokens.
**Recommendations:** Rotate long-lived tokens (GitHub PATs, cloud keys), reduce token lifetime and scope, and apply staged rollout/verification for extension and package updates.
**Source:** A hacker group is poisoning open source code at an unprecedented scale — https://arstechnica.com/information-technology/2026/05/a-hacker-group-is-poisoning-open-source-code-at-an-unprecedented-scale/

### Signed software update supply-chain backdoor on Windows (Daemon Tools)
**Type:** Supply chain compromise / trojanized updates
**Severity:** Medium
**MITRE ATT&CK:** T1195, T1105, T1059
**CVEs:** N/A
**Affected:** Windows endpoints installing Daemon Tools updates
**M365/Azure relevance:** Endpoint compromise remains a common precursor to M365 credential theft, token theft, and subsequent BEC.
**Summary:** Reporting indicates a compromise of update distribution for Daemon Tools where signed installers delivered a multi-stage payload. While many infections were limited to reconnaissance/collection, a subset received more capable backdoors.
**Recommendations:** Verify affected versions, perform endpoint sweep/hunting for code injection and suspicious persistence, and treat impacted endpoints as potential sources of credential theft.
**Source:** Widely used Daemon Tools disk app backdoored in monthlong supply-chain attack — https://arstechnica.com/security/2026/05/widely-used-daemon-tools-disk-app-backdoored-in-monthlong-supply-chain-attack/

## Threat Actor Activity
- **Fox Tempest**: malware-signing-as-a-service abusing Microsoft Artifact Signing and Azure tenant/subscription scale.
- **TeamPCP**: repeated developer-tool supply-chain compromises and token theft used to expand access.
- **Secret Blizzard**: Kazuar malware evolution supporting long-term espionage access.

## Recommended Actions
1. **Reduce token/secret blast radius**: rotate CI/CD tokens immediately after any supply-chain exposure; move to short-lived, scoped credentials wherever possible.
2. **Harden identity paths after non-identity intrusions**: treat edge appliance and endpoint compromise as identity incidents (credential reset + session/token revocation + sign-in anomaly review).
3. **Tighten software supply-chain controls**: stage updates, enforce provenance checks where available, and disable unnecessary auto-update paths for developer tooling.
4. **Patch high-impact post-compromise primitives**: prioritize Linux kernel LPE remediation on cloud hosts, CI runners, and Kubernetes nodes.
5. **Secure agent tooling**: patch agent frameworks, constrain tool/plugin permissions, and add endpoint telemetry/hunting for agent-driven execution.

## Sources
- From edge appliance to enterprise compromise: Multi-stage Linux intrusion via F5 and Confluence — https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/
- Mini Shai Hulud: Compromised @antv npm packages enable CI/CD credential theft — https://www.microsoft.com/en-us/security/blog/2026/05/20/mini-shai-hulud-compromised-antv-npm-packages-enable-ci-cd-credential-theft/
- Exposing Fox Tempest: A malware-signing service operation — https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/
- "Copy Fail" Lands on CISA's KEV: A Nine-Year-Old Linux Bug Becomes a Patch Deadline — https://darkwebinformer.com/copy-fail-lands-on-cisas-kev-a-nine-year-old-linux-bug-becomes-a-patch-deadline/
- When prompts become shells: RCE vulnerabilities in AI agent frameworks — https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/
- A hacker group is poisoning open source code at an unprecedented scale — https://arstechnica.com/information-technology/2026/05/a-hacker-group-is-poisoning-open-source-code-at-an-unprecedented-scale/
- Widely used Daemon Tools disk app backdoored in monthlong supply-chain attack — https://arstechnica.com/security/2026/05/widely-used-daemon-tools-disk-app-backdoored-in-monthlong-supply-chain-attack/
