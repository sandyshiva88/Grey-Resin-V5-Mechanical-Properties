**Mechanical Property Evaluation of Grey Resin V5 Before and After Water Exposure**
<br>
**Author: Sandeep Kumar**
<br>
This repository presents a detailed experimental study on the mechanical properties of Grey Resin V5, a widely used photopolymer resin in SLA (Stereolithography) 3D printing, before and after 72-hour immersion in deionized water. The study aims to evaluate the degradation effects due to water absorption, simulating humid or submerged environmental conditions.

**📌 Overview**
Material: Formlabs Grey Resin V5

Printing Technology: SLA (Stereolithography)

Printer Used: Formlabs Form 4

Test Specimens: Tensile, Flexural, and Impact

Layer Thicknesses: 100 μm, 50 μm, and 25 μm

Exposure Condition: 72-hour immersion in deionized water at ambient conditions

Objective: Evaluate and compare the mechanical properties before and after water exposure

**🧪 Materials & Methods**
Printing Parameters:

Resin: Grey Resin V5

Layer Thickness: 100 μm, 50 μm, 25 μm

Orientation: As per standard mechanical test guidelines (ASTM D638, D790, D256)

Post-Processing:

15 minutes UV post-curing at 60°C using Form Cure

Water immersion of cured specimens for 72 hours

Mechanical Tests Conducted:

Tensile Strength and Modulus (ASTM D638)

Flexural Strength and Modulus (ASTM D790)

Impact Resistance (Izod test – ASTM D256)

**📊 Results Summary**
Property	Condition	Effect After 72h Water Exposure
Tensile Strength	Pre vs Post	Decrease observed
Flexural Strength	Pre vs Post	Moderate reduction
Impact Strength (Izod)	Pre vs Post	Noticeable degradation
Visual Observations	Swelling, color changes	Minor swelling detected

**📁 Detailed plots and raw data are available in the /data and /plots directories.**

🧠 How to Use This Repository
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/grey-resin-water-degradation.git
Install required libraries (if analysis scripts are provided):

bash
Copy
Edit
pip install -r requirements.txt
Run the analysis:
Open analyze_properties.py or Jupyter_Notebook.ipynb for data visualization and summary statistics.

🗂️ Folder Structure
bash
Copy
Edit
📁 grey-resin-water-degradation/
├── data/                  # Raw and processed mechanical test data
├── plots/                 # Graphs and visualizations
├── scripts/               # Python scripts for analysis
├── figures/               # Figures used in any reports or papers
├── README.md              # Project overview and usage
├── requirements.txt       # Python dependencies
└── LICENSE                # License information (MIT or your choice)

🔬 Future Scope
Incorporate machine learning models to predict property degradation

Study the effects of longer immersion times (e.g., 1 week, 1 month)

Expand to other photopolymer resins (e.g., Tough 2000, Elastic 50A)

Conduct thermal and chemical resistance analysis post-immersion

📄 License
Kindly take the prior permission before using it.

**🙏 Acknowledgments**
This work was conducted as part of a broader research study on the environmental and mechanical stability of SLA 3D printed resins.
