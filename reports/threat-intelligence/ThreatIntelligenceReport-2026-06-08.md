# Threat Intelligence Report — 2026-06-08

## Executive Summary
The newest material in the tagged Reader pool is dominated by software supply-chain activity targeting developer workstations, GitHub Actions, and cloud credential paths rather than fresh Microsoft 365 phishing or AiTM reporting. The most serious risk is the Red Hat npm "Miasma" compromise, which stole GitHub, Azure, Key Vault, and other cloud credentials from trusted CI/CD flows and republished poisoned packages with authentic provenance.

The direct M365/AiTM/BEC slice of the `threat intelligence` tag set is stale as of 2026-06-08; that is a collection and tagging problem in Reader, not evidence of a new surge in current M365 phishing coverage. The current week’s relevant risk to Entra ID, Azure, and Microsoft 365 is indirect but material: compromised build systems, abused Azure trust relationships, and signed malware delivery that can lead to identity theft and ransomware.

## Key Threats

### Red Hat npm "Miasma" supply-chain compromise
**Type:** Supply-chain credential theft  
**Severity:** Critical  
**MITRE ATT&CK:** T1195.001, T1059.007, T1528, T1552.001  
**CVEs:** None cited  
**Affected:** `@redhat-cloud-services` npm packages, GitHub Actions runners, Azure IMDS, Microsoft Graph, Azure Key Vault, AWS, GCP, Kubernetes, HashiCorp Vault  
**M365/Azure relevance:** The payload explicitly harvested Azure IMDS OAuth tokens for `management.azure.com`, `graph.microsoft.com`, and Key Vault endpoints, which can expose Azure control plane access and Microsoft 365-linked identities from build infrastructure.  
**Summary:** Microsoft reported a large-scale compromise of Red Hat package publishing that abused a legitimate GitHub Actions OIDC workflow, embedded a preinstall dropper, stole cloud and developer secrets, scraped runner memory for secrets, and republished malicious packages with forged provenance. This is the clearest current-path risk to Azure and Entra-backed engineering environments in the source set.  
**Recommendations:** Rotate Azure, Graph, Key Vault, npm, GitHub, and CI/CD secrets exposed in affected environments; review dependency trees and lockfiles for impacted package versions; disable install scripts where feasible and hunt for Bun execution, GitHub repo creation, and metadata endpoint access from build runners.  
**Source:** [Preinstall to persistence: Inside the Red Hat npm Miasma credential-stealing campaign](https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/)

### Dependency confusion against internal package namespaces
**Type:** Dependency confusion reconnaissance campaign  
**Severity:** High  
**MITRE ATT&CK:** T1195.001, T1027, T1059.007, T1592  
**CVEs:** None cited  
**Affected:** npm clients, internal package scopes, developer endpoints, CI/CD pipelines  
**M365/Azure relevance:** The campaign profiled developer and build hosts that commonly hold Entra, Azure, GitHub, and internal SaaS credentials, creating a low-noise path to later Azure and Microsoft 365 compromise.  
**Summary:** Microsoft uncovered dozens of malicious packages published under fake internal enterprise namespaces. The current payload ran in recon-only mode, fingerprinted hosts, bypassed CI where possible, and used shared infrastructure under the aliases `mr.4nd3r50n`, `ce-rwb`, and `t-in-one`, indicating likely follow-on exploitation against identified high-value environments.  
**Recommendations:** Force internal scopes to resolve only to private registries; block `oob.moika.tech` and hunt for the shared `X-Secret` header and `._*_init.js` artifacts; rotate credentials from any workstation or pipeline that installed the packages.  
**Source:** [Malicious npm packages abuse dependency confusion to profile developer environments](https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/)

### Typosquatted packages stealing cloud and CI/CD secrets
**Type:** Typosquatting-based supply-chain attack  
**Severity:** Critical  
**MITRE ATT&CK:** T1195.001, T1059.007, T1528, T1552.001  
**CVEs:** None cited  
**Affected:** OpenSearch and Elastic-adjacent npm packages, AWS IMDS/ECS, Secrets Manager, Vault, npm, GitHub Actions  
**M365/Azure relevance:** The same execution model applies to Azure-hosted developer and CI/CD systems, especially where GitHub Actions or federated identities bridge into Azure and Microsoft 365 administration.  
**Summary:** A single operator published 14 typosquatted packages that executed at install time, evolved from HTTP-based C2 to Bun-assisted staging, and harvested cloud credentials, Vault tokens, npm publish tokens, and GitHub Actions context. The campaign shows how quickly cloud control paths can be reached through developer dependency mistakes.  
**Recommendations:** Block `aab.sportsontheweb.net` and alert on the `X-Supply: 1` marker; rotate cloud, Vault, npm, and GitHub tokens from exposed hosts; enforce `--ignore-scripts` and review package manifests and lockfiles for the listed package names.  
**Source:** [Typosquatted npm packages used to steal cloud and CI/CD secrets](https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/)

### Compromised `@antv` packages targeting GitHub Actions and cloud secrets
**Type:** Supply-chain compromise of a trusted maintainer  
**Severity:** Critical  
**MITRE ATT&CK:** T1195.001, T1059.007, T1528, T1552.001  
**CVEs:** None cited  
**Affected:** `@antv` npm packages, downstream packages including `echarts-for-react`, GitHub Actions, AWS, Vault, Kubernetes, npm, 1Password  
**M365/Azure relevance:** Any Azure-hosted or Entra-integrated build system consuming affected packages could lose CI/CD tokens, cloud secrets, and repository access that later become entry points into Microsoft 365 and Azure administration.  
**Summary:** Microsoft linked the Mini Shai-Hulud activity to a compromised `@antv` maintainer account. The payload executed during npm install, targeted Linux GitHub Actions runners, scraped runner memory for secrets, stole multi-cloud and package credentials, and used GitHub and public repositories for exfiltration and propagation.  
**Recommendations:** Review direct and transitive dependencies on `@antv`; rotate GitHub, npm, cloud, and vault credentials from affected runners; hunt for Bun execution, suspicious public repositories with the reversed Shai-Hulud marker text, and access to runner memory on Linux build systems.  
**Source:** [Mini Shai Hulud: Compromised @antv npm packages enable CI/CD credential theft](https://www.microsoft.com/en-us/security/blog/2026/05/20/mini-shai-hulud-compromised-antv-npm-packages-enable-ci-cd-credential-theft/)

### Azure-hosted edge compromise pivoting into hybrid identity abuse
**Type:** Multi-stage intrusion and identity compromise  
**Severity:** Critical  
**MITRE ATT&CK:** T1190, T1021.004, T1187, T1557, T1078.002  
**CVEs:** CVE-2025-33073; article also references active exploitation of F5 BIG-IP issues including CVE-2025-53521  
**Affected:** F5 BIG-IP VE in Azure, internal Linux hosts, Atlassian Confluence, Active Directory-connected services  
**M365/Azure relevance:** The initial foothold was an Azure-hosted F5 appliance; the intrusion then abused trust relationships, service credentials, and relay techniques that mirror the same hybrid identity paths used to reach Entra-connected workloads.  
**Summary:** Microsoft documented an intrusion that began from an end-of-life F5 BIG-IP appliance, pivoted to an internal Linux host, then into a vulnerable Confluence instance, and ended with credential theft and Kerberos relay activity against Windows identity infrastructure. It is a strong reminder that Azure-hosted edge assets and internal apps can become the route to broader tenant compromise.  
**Recommendations:** Treat internet-facing Azure edge appliances as Tier-0 assets; patch or retire unsupported F5 and internal Confluence systems; reduce NTLM exposure, enforce SMB and LDAP signing, and monitor cross-system authentication and relay activity from Linux and appliance-originated sessions.  
**Source:** [From edge appliance to enterprise compromise: Multi-stage Linux intrusion via F5 and Confluence](https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/)

### Fox Tempest malware-signing service enabling fake Teams and ransomware delivery
**Type:** Malware-signing-as-a-service  
**Severity:** High  
**MITRE ATT&CK:** T1553.002  
**CVEs:** None cited  
**Affected:** Microsoft Artifact Signing, Azure tenants and subscriptions used for signing, signed malware delivery chains, fake Microsoft Teams installers  
**M365/Azure relevance:** The actor abused Microsoft Artifact Signing through large numbers of Azure tenants and subscriptions, and downstream customers used the signed output to distribute fake Teams installers and ransomware-enabling payloads.  
**Summary:** Microsoft says Fox Tempest created hundreds of Azure tenants and more than a thousand fraudulent signing certificates to provide signed malware to other criminal groups. The service directly enabled campaigns using trojanized Microsoft Teams installers, Oyster backdoors, Lumma, Vidar, and ransomware including Rhysida.  
**Recommendations:** Enforce Safe Links and Safe Attachments, keep SmartScreen and tamper protection enabled, monitor for signed-but-untrusted binaries masquerading as Teams or common admin tools, and review exposure to suspicious short-lived certificates and related Azure artifact-signing activity.  
**Source:** [Exposing Fox Tempest: A malware-signing service operation](https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/)

## Threat Actor Activity
Fox Tempest remains the clearest named actor in the current source set. Microsoft links it to large-scale abuse of Microsoft Artifact Signing and to downstream ransomware and malware operators including Vanilla Tempest, Storm-0501, Storm-2561, and Storm-0249. Its infrastructure and signing workflow materially increase the chance that signed malware will reach users through trusted Microsoft-branded lures such as fake Teams installers.

The rest of the week’s relevant activity is dominated by supply-chain operators rather than classic BEC or AiTM crews. Microsoft attributed one dependency-confusion cluster to the aliases `mr.4nd3r50n`, `ce-rwb`, and `t-in-one`, and a separate typosquatting cluster to `vpmdhaj`. The `@antv` case reflects compromise of a trusted maintainer account rather than a public actor label, but the operational goal is the same: steal credentials from CI/CD systems that often bridge directly into Azure and Microsoft 365 administration.

No fresh M365-specific AiTM or BEC reporting made the latest 20 selected documents. The newest directly relevant feed item in the tagged pool is older, which indicates the Reader collection for this tag needs cleanup if this report is meant to track current Microsoft 365 phishing and identity operations week to week.

## Recommended Actions
1. Audit GitHub Actions, Azure-hosted runners, and developer endpoints for recent installs of affected npm packages; rotate Azure, Graph, Key Vault, GitHub, npm, Vault, and other secrets exposed on those systems.
2. Enforce private-registry scope locking and disable install scripts by default where build processes permit it; flag Bun downloads, unusual Node child processes, and runner memory scraping as high-priority detections.
3. Review Azure-hosted edge appliances and hybrid identity dependencies as Tier-0 assets; retire unsupported F5 versions, patch internal Confluence and similar admin applications, and reduce NTLM relay opportunities.
4. Tighten Microsoft 365 and Entra user protections around signed malware delivery by keeping Safe Links, Safe Attachments, SmartScreen, tamper protection, and attack surface reduction rules enabled.
5. Improve Reader tagging for this workflow so current M365/AiTM/BEC reporting is not buried behind stale or generic threat-intelligence saves.

## Sources
- [Preinstall to persistence: Inside the Red Hat npm Miasma credential-stealing campaign](https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/)
- [Malicious npm packages abuse dependency confusion to profile developer environments](https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/)
- [Typosquatted npm packages used to steal cloud and CI/CD secrets](https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/)
- [Mini Shai Hulud: Compromised @antv npm packages enable CI/CD credential theft](https://www.microsoft.com/en-us/security/blog/2026/05/20/mini-shai-hulud-compromised-antv-npm-packages-enable-ci-cd-credential-theft/)
- [From edge appliance to enterprise compromise: Multi-stage Linux intrusion via F5 and Confluence](https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/)
- [Exposing Fox Tempest: A malware-signing service operation](https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/)
