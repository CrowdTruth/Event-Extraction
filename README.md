# TempEval-3 Dataset: Crowdsourcing Event and Time Expression Annotations

This repository contains (1) the data-agnostic validation methodology of expert-annotated datasets in terms of consistency and completeness and (2) the crowdsourcing annotations for events and time expressions referenced in the following paper:

* Oana Inel and Lora Aroyo: **[Validation Methodology for Expert-Annotated Datasets: Event Annotation Case Study](https:...)**. [Language, Data and Knowledge (LDK), 2019](http://2019.ldk-conf.org).


If you find this data useful in your research, please consider citing:

```
@inproceedings{inel2019validation,
  title={Validation Methodology for Expert-Annotated Datasets: Event Annotation Case Study},
  author={Inel, Oana and Aroyo, Lora},
  booktitle={To Appear in the Proceedings of the 2nd International Conference on Language, Data and Knowledge (LDK)},
  year={2019}
}
```

## Running the notebooks

If you want to run and regenerate the results on your own, you need to install the stable version of the **crowdtruth** package from PyPI using:
```
pip install crowdtruth
```

The data is structured as follows:


## Crowdsourcing Templates
The following crowdsourcing templates have been used in the aforementioned article. We use the same experiment notation as in the article. To check each crowdsourcing annotation template, click on the small template icon. The image will open in a new tab.

| EXP. TYPE| ENTITY TYPE | CROWDSOURCING ANNOTATION TEMPLATE (click to enlarge) | INPUT ENTITY VALUES | ANNOTATION GUIDELINES  | TARGET ANNOTATION |               
|:---:|:----------:|:--------:|:---------------------------:|:--------------------:|:------------------------:|
|P1|   Event  | ![Fig.1: Pilot 1 - Event.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P1_event.png)| Experts (P) & Tools | Explicit Definition |  Entities |
|P1|   Time  | ![Fig.2: Pilot 1 - Time.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P1_time.png)| Experts (P) & Tools | Explicit Definition |  Entities |
|P2|   Event   | ![Fig.3: Pilot 2 - Event.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P2_event.png) |  Experts (P) & Tools | Explicit Definition |  Entities + Motivation (NONE) |
|P2|   Time   | ![Fig.4: Pilot 2 - Time.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P2_time.png) |  Experts (P) & Tools | Explicit Definition |  Entities + Motivation (NONE) |
|P3|   Event | ![Fig.5: Pilot 3 - Event.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P3_event.png) |  Experts (P) & Tools  | Explicit Definition | Entities + Motivation (ALL)|
|P3|   Time | ![Fig.6: Pilot 3 - Time.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P3_time.png) |  Experts (P) & Tools  | Explicit Definition | Entities + Motivation (ALL)|
|P4|   Event | ![Fig.7: Pilot 4 - Event.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P4_event.png) |  Experts (P) & Tools  | Implicit Definition | Entities |
|P4|   Time | ![Fig.8: Pilot 4 - Time.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P4_time.png) |  Experts (P) & Tools  | Implicit Definition | Entities |
|P5|   Event | ![Fig.9: Pilot 5 - Event.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P5_event.png) |  Experts (P) & Tools | Implicit Definition |Entities + Motivation (NONE) |
|P5|   Time | ![Fig.10: Pilot 5 - Time.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P5_time.png) |  Experts (P) & Tools | Implicit Definition |Entities + Motivation (NONE) |
|P6|   Event | ![Fig.11: Pilot 6 - Event.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P6_event.png) |  Experts (P) & Tools  |  Implicit Definition |  Entities + Motivation (ALL) |
|P6|   Time | ![Fig.12: Pilot 6 - Time.](https://raw.githubusercontent.com/CrowdTruth/Event-Extractione/master/templates/P6_time.png) |  Experts (P) & Tools  |  Implicit Definition |  Entities + Motivation (ALL) |
|P7|   Event | ![Fig.13: Pilot 7 - Event.](https://raw.githubusercontent.com/CrowdTruthEvent-Extraction/master/templates/P7_event.png) | Experts (G&P) & Tools & Missing |  Explicit Definition | Entities + Motivation (ALL) |
|P7|   Time | ![Fig.14: Pilot 7 - Time.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P7_time.png) | Experts (G&P) & Tools & Missing |  Explicit Definition | Entities + Motivation (ALL) |
|P8|   Event | ![Fig.15: Pilot 8 - Event.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P8_event.png) | Experts (G&P) & Tools & Missing |  Explicit Definition | Entities + Motivation (ALL) + Highlight |
|P8|   Time | ![Fig.16: Pilot 8 - Time.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/P8_time.png) | Experts (G&P) & Tools & Missing |  Explicit Definition | Entities + Motivation (ALL) + Highlight |
|M1|   Event | ![Fig.17: Main 1 - Event.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/Main_event.png) | Experts (G&P) & Tools & Missing  |  Explicit Definition | Entities + Motivation (ALL) + Highlight |
|M2|   Time | ![Fig.18: Main 2 - Time.](https://raw.githubusercontent.com/CrowdTruth/Event-Extraction/master/templates/Main_time.png) | Experts (G&P) & Tools & Missing  |  Explicit Definition | Entities + Motivation (ALL) + Highlight |
