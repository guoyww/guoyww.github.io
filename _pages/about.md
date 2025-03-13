---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hi, I am a second year Ph.D. student at [Multimedia Laboratory (MMLAB)](https://mmlab.ie.cuhk.edu.hk/), [The Chinese University of Hong Kong](https://www.cuhk.edu.hk/english/index.html), advised by Prof. [Dahua Lin](http://dahua.site/).
Prior to that, I received my Bachelor’s degree in the EE Department at [Nanjing University](https://www.nju.edu.cn/en/).
My research interests focus on deep generative models for visual content creation.  

<!-- <font face="" style="color:#110000"> -->
I am always open to research collaboration & internship opportunities. Feel free to <a href="mailto:guoyw.nju@gmail.com">drop me an email</a> if you are interested in working with me. :)
<!-- </font> -->


# News
- **2024.08**&nbsp; We are organizing the Course on [Generative Models for Visual Content Editing and Creation](https://s2024.conference-program.org/presentation/?id=gensub_279&sess=sess166) at SIGGRAPH 2024.
- **2024.07**&nbsp; SparseCtrl is accepted by ECCV 2024.
- **2023.07**&nbsp; 🎉🎉 AnimateDiff is [online](https://github.com/guoyww/AnimateDiff).
- **2023.06**&nbsp; We are organizing the [Third Workshop on AI for Creative Video Editing and Understanding (CVEU)](https://cveu.github.io/) at ICCV 2023.

# Educations
- **2023.08 - Present**&nbsp; Ph.D. in Information Engineering, The Chinese University of Hong Kong
- **2019.09 - 2023.06**&nbsp; B.Sc. in Electronic Engineering, Nanjing University

# Selected Works
*:equal contribution; †: corresponding author


<!-- LCT -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/papers/long-context-video.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Long Context Tuning for Video Generation**

**Yuwei Guo**,
[Ceyuan Yang](https://ceyuan.me)<sup>†</sup>,
[Ziyan Yang](https://ziyanyang.github.io/),
[Zhibei Ma](https://www.linkedin.com/in/zhibei-ma-30385bb8/),
[Zhijie Lin](https://scholar.google.com/citations?user=xXMj6_EAAAAJ&hl=en),
[Zhenheng Yang](https://zhenheny.github.io/),
[Dahua Lin](http://dahua.site/),
[Lu Jiang](http://www.lujiang.info/)

[**[Paper (coming soon)]**]()&nbsp;
[**[Project]**](https://guoyww.github.io/projects/long-context-video/)&nbsp;
</div>
</div>
<!-- LCT -->


<!-- Repainter -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='images/papers/video-repainter.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**VideoRepainter: Keyframe-Guided Creative Video Inpainting**

**Yuwei Guo**,
[Ceyuan Yang](https://ceyuan.me),
[Anyi Rao](https://anyirao.com),
[Chenlin Meng](https://cs.stanford.edu/~chenlin/),
[Omer Bar-Tal](https://omerbt.github.io/),
[Shuangrui Ding](https://mark12ding.github.io/), \\
[Maneesh Agrawala](http://graphics.stanford.edu/~maneesh/),
[Dahua Lin](http://dahua.site/),
[Bo Dai](https://daibo.info) 

[**[Paper (coming soon)]**]()&nbsp;
[**[Project (coming soon)]**]()&nbsp;
[**[Code (coming soon)]**]()
</div>
</div>
<!-- Repainter -->


<!-- SparseCtrl -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2024</div><img src='images/papers/sparsectrl.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**SparseCtrl: Adding Sparse Controls to Text-to-Video Diffusion Models**

**Yuwei Guo**,
[Ceyuan Yang](https://ceyuan.me)<sup>†</sup>,
[Anyi Rao](https://anyirao.com),
[Maneesh Agrawala](http://graphics.stanford.edu/~maneesh/),
[Dahua Lin](http://dahua.site/),
[Bo Dai](https://daibo.info) 

[**[Paper]**](https://arxiv.org/abs/2311.16933)&nbsp;
[**[Project]**](projects/SparseCtrl/)&nbsp;
[**[Code]**](https://github.com/guoyww/AnimateDiff#202312-animatediff-v3-and-sparsectrl)
</div>
</div>
<!-- SparseCtrl -->


<!-- AnimateDiff -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2024 (spotlight)</div><img src='images/papers/animatediff.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**AnimateDiff: Animate Your Personalized Text-to-Image Models without Specific Tuning**

**Yuwei Guo**,
[Ceyuan Yang](https://ceyuan.me)<sup>†</sup>,
[Anyi Rao](https://anyirao.com),
[Zhengyang Liang](https://maxleung99.github.io),
[Yaohui Wang](https://wyhsirius.github.io), \\
[Yu Qiao](https://scholar.google.com/citations?user=gFtI-8QAAAAJ&hl=en),
[Maneesh Agrawala](http://graphics.stanford.edu/~maneesh/),
[Dahua Lin](http://dahua.site/),
[Bo Dai](https://daibo.info) 

[**[Paper]**](https://arxiv.org/abs/2307.04725)&nbsp;
[**[Project]**](https://animatediff.github.io/)&nbsp;
[**[Code (10k+ stars)]**](https://github.com/guoyww/AnimateDiff)
</div>
</div>
<!-- AnimateDiff -->


<!-- Imagine360 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/papers/imagine360.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Imagine360: Immersive 360 Video Generation from Perspective Anchor**

[Jing Tan](https://sparkstj.github.io),
[Shuai Yang](https://ys-imtech.github.io),
[Tong Wu](https://wutong16.github.io),
[Jingwen He](https://scholar.google.com/citations?user=GUxrycUAAAAJ&hl=zh-CN),
**Yuwei Guo**,
[Ziwei Liu](https://liuziwei7.github.io),
[Dahua Lin](http://dahua.site)

[**[Paper]**](https://arxiv.org/abs/2412.03552)&nbsp;
[**[Project]**](https://ys-imtech.github.io/projects/Imagine360/)&nbsp;
[**[Code]**](https://github.com/YS-IMTech/Imagine360)
</div>
</div>
<!-- Imagine360 -->


<!-- SAM2Long -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/papers/sam2long.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**SAM2Long: Enhancing SAM 2 for Long Video Segmentation with a Training-Free Memory Tree**

[Shuangrui Ding](https://mark12ding.github.io),
[Rui Qian](https://shvdiwnkozbw.github.io),
[Xiaoyi Dong](https://lightdxy.github.io),
[Pan Zhang](https://panzhang0212.github.io),
[Yuhang Zang](https://yuhangzang.github.io),
[Yuhang Cao](https://scholar.google.com/citations?user=sJkqsqkAAAAJ&hl=zh-CN), \\
**Yuwei Guo**,
[Dahua Lin](http://dahua.site),
[Jiaqi Wang](https://myownskyw7.github.io)

[**[Paper]**](https://arxiv.org/abs/2410.16268)&nbsp;
[**[Project]**](https://mark12ding.github.io/project/SAM2Long/)&nbsp;
[**[Code]**](https://github.com/Mark12Ding/SAM2Long)
</div>
</div>
<!-- SAM2Long -->


<!-- CameraCtrl -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/papers/cameractrl.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**CameraCtrl: Enabling Camera Control for Video Diffusion Models**

[Hao He](https://hehao13.github.io),
[Yinghao Xu](https://justimyhxu.github.io),
**Yuwei Guo**,
[Gordon Wetzstein](https://stanford.edu/~gordonwz/),
[Bo Dai](https://daibo.info) 
[Hongsheng Li](https://www.ee.cuhk.edu.hk/~hsli/),
[Ceyuan Yang](https://ceyuan.me)

[**[Paper]**](https://arxiv.org/abs/2404.02101)&nbsp;
[**[Project]**](https://hehao13.github.io/projects-CameraCtrl/)&nbsp;
[**[Code]**](https://github.com/hehao13/CameraCtrl)
</div>
</div>
<!-- CameraCtrl -->


<!-- HumanVid -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024 D&B Track</div><img src='images/papers/humanvid.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**HumanVid: Demystifying Training Data for Camera-controllable Human Image Animation**

[Zhenzhi Wang](https://zhenzhiwang.github.io),
[Yixuan Li](https://yixuanli98.github.io),
[Yanhong Zeng](https://zengyh1900.github.io),
[Youqing Fang](),
**Yuwei Guo**,
[Wenran Liu](),
[Jing Tan](https://sparkstj.github.io),
[Kai Chen](https://chenkai.site),
[Tianfan Xue](https://tianfan.info),
[Bo Dai](https://daibo.info),
[Dahua Lin](http://dahua.site/)

[**[Paper]**](https://arxiv.org/abs/2407.17438)&nbsp;
[**[Project]**](https://humanvid.github.io/)&nbsp;
[**[Code]**](https://github.com/zhenzhiwang/HumanVid)
</div>
</div>
<!-- HumanVid -->


<!-- Dynamic Storyboard -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SIGGRAPH Poster</div><img src='images/papers/sig23vds.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Dynamic Storyboard Generation in an Engine-based Virtual Environment for Video Production**

[Anyi Rao](https://anyirao.com)<sup>\*</sup>,
[Xuekun Jiang]()<sup>\*</sup>,
**Yuwei Guo**,
[Linning Xu](https://eveneveno.github.io/lnxu/),
[Lei Yang](https://yanglei.me),
[Libiao Jin](),
[Dahua Lin](http://dahua.site/),
[Bo Dai](https://daibo.info) 

[**[Paper]**](https://arxiv.org/abs/2301.12688)&nbsp;
[**[Project]**](https://virtualfilmstudio.github.io/)
</div>
</div>
<!-- Dynamic Storyboard -->

# Experiences
- **Research Intern**, ByteDance Seed, Shanghai, China (2024.12 - present)  
  with [Ceyuan Yang](https://ceyuan.me)

- **Research Intern**, Pika Labs, Palo Alto, USA (2024.06 - 2024.08)  
  with [Chenlin Meng](https://cs.stanford.edu/~chenlin/), [Omer Bar-Tal](https://omerbt.github.io)

- **Research Intern**, Shanghai AI Laboratory, Shanghai, China (2022.10 - 2023.08)  
  with [Ceyuan Yang](https://ceyuan.me), [Bo Dai](https://daibo.info), [Anyi Rao](https://anyirao.com)

# Selected Awards
- **2023.04**&nbsp; Hong Kong PhD Fellowship
- **2023.04**&nbsp; CUHK Vice-Chancellor's Scholarship
- **2020.10**&nbsp; China National Scholarship

# Talks
- **2023.11**&nbsp; Invited talk at Kunlun 2050 Research

# Reviewer
- **2025**&nbsp; CVPR, SIGGRAPH, ICML, ICCV, NeurIPS
- **2024**&nbsp; SIGGRAPH, ACM MM, SIGGRAPH Asia, NeurIPS, ICLR, CVPR

# Teaching
- IERG4998&nbsp; Final Year Project, Fall 2023
- IERG4998&nbsp; Final Year Project, Spring 2024
