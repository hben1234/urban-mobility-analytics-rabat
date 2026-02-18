# Transport Accessibility Analysis (SDG 11.2.1) - Rabat-Salé-Kénitra Region

## Project Overview

This project, developed at the **Haut-Commissariat au Plan (HCP)**, evaluates equitable access to public transport for 2 million inhabitants in Morocco's Rabat-Salé-Kénitra region. The goal is to calculate the **SDG 11.2.1** indicator using open data and spatial analysis.

> **Key Impact:** Identified 278,000 inhabitants in "mobility fracture" zones, enabling targeted public investments.

## Technical Stack
- **GIS & Geomatics:** QGIS, PyQGIS (Python scripting), OpenStreetMap (Overpass Turbo)
- **Data Engineering:** Spatial ETL, Geographic joins, Hexagonal grids (H3)
- **Business Intelligence:** Power BI, Advanced DAX, Star schema modeling

## Methodology (Geospatial ETL)
1. **Extraction:** Mining OSM data (bus stops, tram, train) via Overpass API
2. **Spatial Transformation (QGIS):**
   - Generation of isochrone buffers (500m)
   - Population density correction via Python script (weighting by intersected surface)
3. **Visualization (Power BI):**
   - Strategic recommendation algorithm in DAX
   - Interactive dashboard for public decision-making

## Installation

### Prerequisites
- QGIS 3.28+ with Python support
- Python 3.9+
- Git

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sdg11-transport-accessibility.git
   cd sdg11-transport-accessibility
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or using Conda:
   ```bash
   conda env create -f environment.yml
   conda activate sdg11-transport-env
   ```

3. Open the QGIS project (`data/processed/qgis_project.qgz`) and load required layers.

## Usage

### Data Processing
1. Load raw data from `data/raw/`
2. Run QGIS scripts in order:
   ```python
   # In QGIS Python console
   exec(open('scripts/qgis/corrected_population.py').read())
   exec(open('scripts/qgis/transport_score.py').read())
   ```
3. Processed data will be saved in `data/processed/`

### Visualization
- Open `powerbi/dashboard.pbit` for interactive analysis
- Screenshots available in `powerbi/screenshots/`

## Project Structure
```
sdg11-transport-accessibility/
├── data/
│   ├── raw/                 # Input data
│   └── processed/           # Generated outputs
├── scripts/
│   └── qgis/                # QGIS Python scripts
├── powerbi/                 # Power BI assets
├── config/                  # Configuration files
├── requirements.txt         # Python dependencies
├── environment.yml          # Conda environment
├── LICENSE                  # MIT License
└── README.md
```

## Results
- **Transport Accessibility Score:** 86,4% (calculated dynamically)
- **Population Served:** 1,722,000 out of 2,000,000
- **Mobility Gaps Identified:** 278,000 inhabitants

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push and create a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- **Organization:** Haut-Commissariat au Plan (HCP)
- **Project Lead:** Houda Bennani
- **Email:** [houda.bennani.pro@gmail.com]

---

*This analysis contributes to Morocco's commitment to SDG 11: Make cities inclusive, safe, resilient, and sustainable.*



