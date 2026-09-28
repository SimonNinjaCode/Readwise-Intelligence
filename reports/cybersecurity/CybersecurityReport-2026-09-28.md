# Cybersecurity Report — 2026-09-28

## Week in Security

The dominant theme is operational convergence: ransomware affiliates, identity phishing, advertising fraud, and AI-agent abuse are increasingly exploiting the same weak controls—browser trust, excessive identity permissions, unmanaged remote tooling, and poor visibility. Storm-2570 shows why defenders should track post-compromise behaviour across payloads rather than keying detection only to a ransomware brand. EvilTokens turns device-code phishing into a scalable service, while Microsoft’s September security updates extend Zero Trust and data controls to agent traffic. The collection itself remains uneven: the full `later` + `feed` pool contained 968 tagged documents, but the newest 20 were all from `later`; the tagged `feed` material is materially older and should be treated as a stale collection/tagging problem, not as current weekly coverage.

## Notable Incidents & Breaches

- **Storm-2570 ransomware affiliate.** Microsoft links the affiliate to Qilin, DragonForce, Anubis, and BERT deployments across healthcare, government, education, finance, energy, retail, manufacturing, and other sectors. The recurring pattern is remote-management tooling, credential access, lateral movement, security tampering, cloud exfiltration, and only then ransomware. The lesson is to detect the intrusion chain before encryption and correlate RMM, privilege, and exfiltration signals across ransomware families. [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/)

- **EvilTokens device-code phishing platform.** Microsoft describes a PhaaS operation using AI-assisted lures, automated infrastructure, and token theft; Microsoft and partners disrupted parts of its infrastructure. The affected population is broad by design: device-code flows allow attackers to convert a convincing prompt into access tokens without stealing a password. Block or tightly scope device-code authentication, monitor unusual OAuth/device-code activity, and revoke sessions after suspected token capture. [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/), [Ars Technica](https://arstechnica.com/security/2026/09/microsoft-disrupts-ai-assisted-platform-that-compromised-12000/)

- **Google-ad tech-support scam.** Netskope observed malicious ads reaching users in 619 customer organisations between 31 August and 14 September, across at least 284 legitimate publisher sites. The campaign used browser-based scareware that simulated a locked Windows or Mac device and directed victims to a fraudulent call centre for payment, remote access, or personal data. Ad-supply-chain controls, browser isolation, user reporting, and clear help-desk guidance matter because the payload manufactures urgency rather than relying on a conventional malware install. [Ars Technica](https://arstechnica.com/security/2026/09/google-ads-caught-delivering-convincing-scareware-ads-to-unsuspecting-users/)

- **International Meteor Organization outage.** The nonprofit reported that a cyberattack dealt a “critical blow” to ageing infrastructure and would cause weeks of partial downtime. No actor, ransom demand, or confirmed data theft was reported. The incident is a reminder that small organisations with public data remain operationally exposed when recovery depends on ageing, poorly replaceable systems. [Ars Technica](https://arstechnica.com/security/2026/09/nonprofit-that-tracks-meteors-taken-down-by-critical-blow-from-a-cyberattack/)

## Vulnerabilities & Patches

- **AI-agent privilege exposure.** A reported zero-day in Meta’s Muse assistant shows how a privileged agent can be hijacked through a simple ClickFix-style interaction. The practical risk is not the label “AI”; it is an agent with browser, data, and action privileges operating on behalf of a user. Treat agent permissions as application permissions: minimise tools and data access, isolate execution, require confirmation for consequential actions, and log tool calls. [Ars Technica](https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/)

- **RSA and cryptographic transition risk.** Ars reports a new faster approach to breaking RSA assumptions. The item is research reporting, not a disclosed CVE or an immediate production exploit, so it should not trigger emergency key rotation on its own. It does justify inventorying RSA dependencies, prioritising crypto-agility, and keeping post-quantum migration plans tied to certificate and application lifecycles. [Ars Technica](https://arstechnica.com/security/2026/09/theres-a-new-way-to-break-rsa-thats-faster-than-anything-weve-seen-before/)

- **No CVE-specific patch item in this selection.** The selected pool did not provide a sufficiently detailed, current CVE or CVSS 9+ advisory. Patch prioritisation should therefore continue from the organisation’s own exposure and active-exploitation telemetry rather than being inferred from this week’s Reader sample.

## Threat Actor Activity

- **Storm-2570** operates as a cross-ecosystem ransomware affiliate. Its stable tooling and tradecraft are more useful for detection than the final ransomware family.

- **EvilTokens** demonstrates the industrialisation of device-code phishing: lure creation, infrastructure, and token theft are packaged for scale. Identity telemetry and conditional access controls need to detect the flow, not merely the login result.

- **TeamPCP** remains a supply-chain concern. Reporting describes a Google analyst infiltrating the group’s inner circle, reinforcing that developer and package ecosystems are active intrusion surfaces rather than secondary hygiene issues. [Ars Technica](https://arstechnica.com/security/2026/09/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/)

## Cloud & Identity Security

- Microsoft’s September security updates add local AI-agent inventory, extend Zero Trust concepts to agent traffic, and combine Purview classification with Entra Global Secure Access to block sensitive data moving to unsanctioned AI services. The control objective is sound: enforce data policy at the network boundary for both human and on-behalf-of agent traffic. Validate coverage, exceptions, and false positives before treating the feature as a completed control. [Microsoft Security](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/)

- Microsoft Entra’s current direction is identity-driven access rather than broad network reach. The selected material points to B2B passkeys, tenant-estate governance, identity lifecycle automation, and replacing VPN access with per-application access. The usable security outcome is reduced standing access—provided tenant inventory, application ownership, stale credentials, and lifecycle events are actually governed. [Entra News](https://entra.news/p/entra-news-167-this-week-in-microsoft), [Entra tenant governance](https://techcommunity.microsoft.com/t5/microsoft-entra-blog/prepare-your-tenant-estate-for-ai-join-our-upcoming-webinars/ba-p/4554525)

- Maester 2.2 adds 269 opt-in Active Directory checks across 19 areas, including GPO state, DACLs, DNS, trusts, replication, and schema. The value is repeatable assurance across on-premises identity, but the tests are read-only checks—not proof that tiering or privileged access is effective. [Entra News](https://entra.news/p/active-directory-security-testing)

## Recommended Actions

1. **Harden device-code authentication now.** Restrict the flow where possible, require phishing-resistant authentication for privileged users, alert on anomalous device-code grants, and rehearse token revocation.
2. **Hunt for ransomware precursors.** Correlate RMM deployment, credential dumping, lateral movement, security-tool tampering, cloud-storage staging, and unusual exfiltration independently of the final payload.
3. **Reduce agent privilege.** Inventory local and cloud agents, remove unnecessary tools and data access, isolate execution, and require approval for external communication or destructive actions.
4. **Test identity posture.** Run the new AD checks in a controlled tier-zero context, review stale Entra applications and credentials, and validate joiner/mover/leaver automation.
5. **Close the browser and ad-tech gap.** Provide a one-page tech-support-scam playbook, block unauthorised remote support, and ensure users know that a browser warning must never be answered by calling its displayed number.
6. **Start crypto-agility inventory.** Map RSA certificates, keys, libraries, and protocol dependencies; prioritise systems with long replacement cycles.

## Sources

- [Your uncle’s frozen Mac says it’s infected after viewing a Google ad. Now what?](https://arstechnica.com/security/2026/09/google-ads-caught-delivering-convincing-scareware-ads-to-unsuspecting-users/)
- [What’s new in Microsoft Security: September 2026](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/)
- [Beyond the ransomware: Tracking Storm-2570’s consistent tradecraft across deployments](https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/)
- [There’s a new way to break RSA that’s faster than anything we’ve seen before](https://arstechnica.com/security/2026/09/theres-a-new-way-to-break-rsa-thats-faster-than-anything-weve-seen-before/)
- [Microsoft disrupts AI-assisted platform that compromised 12,000](https://arstechnica.com/security/2026/09/microsoft-disrupts-ai-assisted-platform-that-compromised-12000/)
- [Unmasking EvilTokens: Getting to the root of device code phishing](https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/)
- [Muse, Meta’s extraordinarily privileged AI assistant, has a serious 0-day](https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/)
- [An undercover Google analyst infiltrated a notorious supply-chain hacking gang](https://arstechnica.com/security/2026/09/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/)
- [Entra 🆔 News #167 → This week in Microsoft Entra](https://entra.news/p/entra-news-167-this-week-in-microsoft)
- [Prepare your tenant estate for AI: Join our upcoming webinars](https://techcommunity.microsoft.com/t5/microsoft-entra-blog/prepare-your-tenant-estate-for-ai-join-our-upcoming-webinars/ba-p/4554525)
- [Active Directory Security Testing in Maester 2.2](https://entra.news/p/active-directory-security-testing)
- [Nonprofit that tracks meteors taken down by “critical blow” from a cyberattack](https://arstechnica.com/security/2026/09/nonprofit-that-tracks-meteors-taken-down-by-critical-blow-from-a-cyberattack/)
