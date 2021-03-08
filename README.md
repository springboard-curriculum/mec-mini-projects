# Machine Learning Engineering Course Mini-Projects

This is the repository of the current miniprojects for Springboard's Machine Learning Engineering course. As you work through the curriculum, you will need to complete each and everyone of those mini-projects and review and discuss them with your mentor.

It is highly recommended to fork this repository on Github and share it with your mentor so that they can easily follow your progress.

## Installation

Below are details instructions on how to get those mini projects up and running. None of those projects should require tons of CPU or memory, so you are welcome to either run those locally on your computer, or through any hosted jupyter notebook services such as Deepnote or Google's Collab.

### Local

To run those projects locally, we recommend you first install Anaconda for your operating system (Windows, Mac, Linux) by downloading it and following the instructions here: https://www.anaconda.com/products/individual#Downloads

Once anaconda is installed, run the following command to create dedicated python environment with all the libraries and packages needed to run all the mini projects in this repo:
```conda env create -f environment.yml```

Then activate the environment by running:
```conda activate mec-miniprojects```

Then create an ipython kernel for Jupyter based on this environment:
```python -m ipykernel install --user --name mec-miniprojects --display-name "Python (MEC Mini-Projects)"```

Finally, launch Jupyter Lab and navigate to each mini-project notebook and make sure to select the kernel that was created above:
```jupyter lab```

### Google Colab

It is actually very easy to work and run the notebooks for each mini-projects in Google Colab by leveraging the Github integration. Please note that you will need to have forked the mini-projects repository for this to work.

Here are the steps:
- Go to: https://colab.research.google.com/ (and login with a Google account)
- Select File -> Open Notebook
- Select the Github Tab in the popup window which opened
- Login with your Github Account, and allow Google Colab to have ready/write access to your personal private repositories
- Once the authorization processed, you should now see a list of all your repositories on Github. All you need to do for this step is to select the forked mec-mini-projects repo
- Once the mec-mini-projects repo selected Colab will ask you which notebook you want to open in that repo. 
- After selecting the mini-project notebook of your choice, it will be open and ready to use

Once you are done working on your mini-project notebook in Colab, you can easily save a copy of your notebook back to Github by clicking on File -> Save a Copy To Github, it will ask you to enter a commit message, and a file name, and will then commit your changes and work to Github.

#### Cautionary words
Google Collab, while being super easy to get up and running and a very capable environment for all the MEC mini-projects, does have one main drawback: python library versions. You are able to easily install packages, but Colab comes with a fleet of existing datascience related packages, and they may not always be the same version that is expected in the various mini-projects. There can be sometimes some incompatibilities, requiring you to install or upgrade some of the packages needed.

## Contributions & PRs welcome!

With the objective to proviide the best possible learning content to our students, please do note hesitate to open issues in Github or submit PRs if you catch any typos or issues in those mini-projects.




