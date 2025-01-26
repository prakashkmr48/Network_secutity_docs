import os

# Directory for Sphinx source files
source_dir = "source"

# Ensure the source directory exists
os.makedirs(source_dir, exist_ok=True)

# File names and their content
files_content = {
    "index.rst": """\
Network Security Documentation
==============================

Welcome to the network security documentation! Navigate through the sections below to learn about best practices, tools, and key concepts.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   best_practices
   tools
   glossary

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
""",
    "introduction.rst": """\
Introduction to Network Security
================================

Network security involves protecting a computer network and its data from unauthorized access, misuse, or harm.

Why is network security important?
-----------------------------------
- Prevents data breaches and theft.
- Ensures compliance with regulations.
- Protects user and organizational trust.

Key Threats
-----------
- Malware (viruses, ransomware).
- Phishing attacks.
- Denial of Service (DoS) attacks.
- Man-in-the-Middle (MitM) attacks.
""",
    "best_practices.rst": """\
Network Security Best Practices
===============================

1. Use Firewalls
   ----------------
   Firewalls act as the first line of defense, blocking unauthorized access to your network.

2. Implement Strong Password Policies
   -----------------------------------
   - Use complex passwords with at least 12 characters.
   - Enable multi-factor authentication (MFA).

3. Regularly Update Software
   --------------------------
   Keep all systems, applications, and firmware updated to patch known vulnerabilities.

4. Monitor Network Traffic
   ------------------------
   Use tools like Wireshark or SolarWinds to detect unusual activity.

5. Conduct Regular Security Training
   ----------------------------------
   Educate employees about phishing, social engineering, and secure practices.
""",
    "tools.rst": """\
Network Security Tools
======================

1. Wireshark
   ----------
   A powerful packet analyzer for network troubleshooting and analysis.

2. Nessus
   -------
   A vulnerability scanner that identifies security weaknesses in your network.

3. Snort
   ------
   An open-source intrusion detection and prevention system (IDS/IPS).

4. Metasploit
   -----------
   A penetration testing framework used to identify vulnerabilities.

5. Nmap (Network Mapper)
   ----------------------
   A tool for network discovery and security auditing.
""",
    "glossary.rst": """\
Glossary of Terms
=================

Firewall
    A security system that monitors and controls incoming and outgoing network traffic.

Phishing
    A cyberattack where attackers trick users into revealing sensitive information.

Intrusion Detection System (IDS)
    A system that monitors network traffic for suspicious activities.

Man-in-the-Middle (MitM) Attack
    A type of cyberattack where the attacker intercepts communication between two parties.

Encryption
    The process of encoding data to protect it from unauthorized access.
""",
}

# Create each file with its content
for filename, content in files_content.items():
    filepath = os.path.join(source_dir, filename)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

print(f"All files have been created in the '{source_dir}' directory.")
