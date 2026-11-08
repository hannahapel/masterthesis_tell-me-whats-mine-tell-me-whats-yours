"""Framework Applicability Pilot — reproducible sampling.
Source: Scoping_CMs final(5).xlsx, References and Scoping Deepfake CM.
Study order follows References. IDs are matched from the concept matrix.
NOTE: Reproduction requires the same input order and original sampling method.
"""
import random
from collections import defaultdict

papers = [('#01', 'Is sharing caring? Deepfakes and gender-based violence in MENA'),
 ('#02',
  'A deep fake detection approach for cyber security threat based on deep learning and diffusion-osmosis model'),
 ('#03', 'Synthetic Lies: Security and Ethical Challenges of Deceptive Content in Generative AI'),
 ('#04',
  'Optimizing Deepfake Image Classification with Transfer Learning: Insights from Models Inception V3 and '
  'Inception V4'),
 ('#05',
  'AI-Driven Synthetic Threats in Cybersecurity: A User-Centered Framework for Awareness, Detection, and '
  'Protective Behavior'),
 ('#06', 'Ethical Foundations of AI-Driven Avatars in the Metaverse for Innovation and User Privacy'),
 ('#07',
  'CNN-GMM approach to identifying data distribution shifts in forgeries caused by noise: a step towards '
  'resolving the deepfake problem'),
 ('#08', 'A systematic review of audio deepfake detection techniques for digital investigation'),
 ('#09', 'Seeing Is Not Believing: A Deepfake Video Call Scam at Pan-Asia Trading'),
 ('#10', 'Video Deepfake Detection: Current Trends, Methodologies, and Future Directions'),
 ('#11', 'Unsafe workplaces, marketed students: The deepfake policy gap in education'),
 ('#12', 'Exposing Deepfakes: A Comprehensive Approach to Video Authenticity Verification via Uploads and URLs'),
 ('#13', 'The Creation of Digital Deception: An Examination of the Development of Deep fakes'),
 ('#14', 'EffiSwinNet: A Cross-Architecture Deepfake Detection with Style GAN Generated Faces'),
 ('#15', 'Synthetic ID Card Image Generation for Improving Presentation Attack Detection'),
 ('#16',
  'Do You Trust Me? – Development of a Framework to Analyze the Role and Meaning of Trustworthiness of Avatars'),
 ('#17', 'Deep Data Hiding for ICAO-Compliant Face Images: A Survey'),
 ('#18', 'Sexual Privacy'),
 ('#19',
  'ARTIFICIAL INTELLIGENCE IN CYBERSECURITY: EXAMINING LIABILITY, CRIME DYNAMICS, AND PREVENTIVE STRATEGIES'),
 ('#20', 'Online Child Sexual Exploitation: A New MIS Challenge'),
 ('#21', 'Malinformation, Deepfakes, and Cyber Warfare: Ethical and Anticipated Ethical Issues'),
 ('#22',
  'The Generative AI Paradox: GenAI and the Erosion of Trust, the Corrosion of Information Verification, and the '
  'Demise of Truth'),
 ('#23', 'Criminalizing Deepfakes: A Comprehensive Review of US Legislative Responses to Synthetic Media Abuse'),
 ('#24', 'Seeing is No Longer Believing: How Deepfakes May Shape the Future of Identity Credibility in Media'),
 ('#25', 'AI-Based Detection of Deepfake Videos'),
 ('#26', 'Deepfakes: current and future trends'),
 ('#27', 'FFDL: Feature Fusion-Based Deep Learning Method Utilizing Federated Learning for Forged Face Detection'),
 ('#28', 'Deep Learning-Based Face Forgery Detection for Facial Payment Systems'),
 ('#29', '‘It’s still abuse’: community attitudes and perceptions on AI-generated image-based sexual abuse'),
 ('#30', 'DEFENDING REALITY: HUMAN-AI COLLABORATION TO UNVEIL DEEPFAKE INFORMATION MANIPULATION'),
 ('#31',
  'Synthetic Lies, Digital Truths: A Systematic Review of Computer-Mediated Deception Research in the Era of AI '
  'and Deepfakes'),
 ('#32', 'Sociotechnical Dynamics of Deepfake Creation: An Activity Systems Analysis'),
 ('#33',
  'Rewriting the stars: Surface tensions and gender troubles in the online media production of digital deepfakes'),
 ('#34', 'AI-Powered Cybercrime: A Survey on Emerging Threats, Tools & Techniques for Countermeasures'),
 ('#35',
  'Context-Aware Misinformation Detection: A Benchmark of Deep Learning Architectures Using Word Embeddings'),
 ('#36',
  'Generative AI-driven synthetic media risks in digital health: implications for telemedicine and teledentistry'),
 ('#37',
  'Shadows of Selfies: How Generative AI Fuels GBV-An Analysis of Non-consensual Sexualised Deepfakes Through '
  'Abolitionism and Intersectionality'),
 ('#38', 'Deep Fake Audio and the Ethical Dilemmas of AI in Podcasting'),
 ('#39', 'Secure and Reversible Face De-Identification With Format-Preserving Encryption'),
 ('#40', 'Deepfakes and image manipulation: criminalisation and control'),
 ('#41', 'Vulnerability of Automatic Identity Recognition to Audio-Visual Deepfakes'),
 ('#42',
  'LLMs-based Thematic Analysis of Social Media Deepfakes and its Empirical Parallelism with Deepfake News'),
 ('#43', 'Who is driving this deepfake? Beyond Deepfake Detection with Driver Identification'),
 ('#44',
  'AI Deepfake Interaction, Authentication and Correction in Taiwan: Examining the Roles of Echo Chamber and '
  'Conspiracy Mentality'),
 ('#45', 'Information Credibility: Evidence Warranted in Synthetic Media Environments'),
 ('#46',
  'Multimodal Enterprise Authentication Resistant to AI-Based Identity Manipulation: Facial Anti-Spoofing and '
  'Multilingual Deepfake Speech Detection'),
 ('#47', 'Criminal Liability for the Violation of Identity Using Deepfakes in South Africa'),
 ('#48',
  'FCRL-Net: Identity-Invariant Forgery-Centric Representation Learning for Generalizable and Audio Deepfake '
  'Detection'),
 ('#49', 'Copyright or personality rights? A critical analysis of Denmark’s approach to deepfakes'),
 ('#50', 'PITCH: AI-assisted Tagging of Deepfake Audio Calls using Challenge-Response'),
 ('#51', 'Face Swap Detection using Deep Learning Techniques'),
 ('#52', 'Deepfakes: Deceptions, mitigations, and opportunities'),
 ('#53', 'Anti-Forensic Deepfake Personas and How To Spot Them'),
 ('#54',
  'Systematic Review of Fake News, Propaganda, and Disinformation: Examining Authors, Content, and Social Impact '
  'Through Machine Learning'),
 ('#55', 'Deepfake Shield: An Intelligent Deepfake Detection System'),
 ('#56', 'An Advanced Hybrid Deep Learning Fusion Framework for Fake Profile Identification on Social Platforms'),
 ('#57', 'The Corrosion of Truth: Deepfakes and the Evolving Trouble to Digital Identity'),
 ('#58', 'Group Decision Performance of Human Examiners for Identity-aware Face Image Manipulation Detection'),
 ('#59', 'MSF-RGBNet: A Lightweight Multi-Stage Fusion Architecture for Deepfake Image Detection'),
 ('#60', 'Deepfake videos: synthesis and detection techniques – a survey.'),
 ('#61', 'A comprehensive evaluation of feature-based AI techniques for deepfake detection'),
 ('#62', 'Combating Falsification of Speech Videos with Live Optical Signatures'),
 ('#63', 'Artificial Intelligence Is No Match for Human Stupidity: Ethical Reflections on Avatars and Agents'),
 ('#64',
  'Preserving Information Integrity: Analyzing the Impact of Deepfake Videos on Social Media Trust and Security'),
 ('#65', 'Revisiting Biometrics in Cybersecurity: Do AI Methods and Zero-Trust Architectures Drive Innovation?'),
 ('#66',
  'Combating Identity Forgery in Social Media: Detecting Manipulated Profile Videos With a Motion-Texture Fusion '
  'Framework'),
 ('#67', 'Deepfakes and beyond: A Survey of face manipulation and fake detection'),
 ('#68', 'Combatting Deepfake Misinformation on Social Media: A Scoping Review and Research Agenda'),
 ('#69', 'Recapture Detection to Fight Deep Identity Theft'),
 ('#70',
  'What Is So Deep About Deepfakes? A Multi-Disciplinary Thematic Analysis of Academic Narratives About Deepfake '
  'Technology'),
 ('#71', 'Deepfakes: An Integrative Review of the Literature and an Agenda for Future Research'),
 ('#72', 'Seeing Through Deepfakes: Explainable AI (XAI) for Image Forensics and Visual Detection'),
 ('#73',
  'Protection Of Sensitive Personal Information Contained In Digital Files Held By Individuals With Homomorphic '
  'Encryption And AI Assistance'),
 ('#74',
  'Defeating Multimodal Information Manipulation By A Web 3.0 Decentralized Identity (DID)-Based Accountability '
  'Framework'),
 ('#75', 'Fighting Malicious Media Data: A Survey on Tampering Detection and Deepfake Detection'),
 ('#76', 'DeepFake on Face and Expression Swap: A Review'),
 ('#77', 'Legal Protection against Digital Personal Identity Fraud in South Africa'),
 ('#78', 'Synthetic Realities: A Critical Review'),
 ('#79', 'Deepfake CAPTCHA: A Method for Preventing Fake Calls'),
 ('#80',
  'Algorithmic Directors and Performative Ghosts: The Ethics of Actor Identity in the Age of Generative AI.')]

def classify(title):
    t = title.lower()
    review_kw = ['survey', 'review', 'systematic', 'scoping', 'integrative',
                 'thematic analysis', 'critical review']
    legal_kw = ['legal', 'liability', 'criminal', 'criminalis', 'criminaliz',
                'copyright', 'law', 'protection of', 'fraud in south africa']
    social_kw = ['ethic', 'trust', 'gender', 'abuse', 'sexual', 'avatar',
                 'privacy', 'identity credibility', 'stupidity', 'gbv',
                 'violence', 'gender troubles', 'community attitudes']
    tech_kw = ['detection', 'deep learning', 'classification', 'learning-based',
               'fusion', 'network', 'forensic', 'captcha', 'encryption',
               'authentication', 'biometric', 'anti-spoofing']
    if any(k in t for k in review_kw):
        return 'Review/Survey'
    if any(k in t for k in legal_kw):
        return 'Legal/Policy'
    if any(k in t for k in social_kw):
        return 'Social/Ethics'
    if any(k in t for k in tech_kw):
        return 'Technical/Detection'
    return 'Other'

groups = defaultdict(list)
for paper in papers:
    groups[classify(paper[1])].append(paper)

random.seed(42)
purposive = []
for group in ['Review/Survey', 'Legal/Policy', 'Social/Ethics', 'Technical/Detection']:
    if not groups[group]:
        raise ValueError(f'No papers classified as {group}')
    purposive.append((group, random.choice(groups[group])))

used_ids = {paper[0] for _, paper in purposive}
remaining = [paper for paper in papers if paper[0] not in used_ids]
random_sample = random.sample(remaining, 6)

print('Study type counts:', {group: len(items) for group, items in groups.items()})
print('Purposive selections:')
for group, (study_id, title) in purposive:
    print(f'  {group}: {study_id} — {title}')
print('Random selections:')
for study_id, title in random_sample:
    print(f'  {study_id} — {title}')
