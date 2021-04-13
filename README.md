# Machine Learning Engineering Course Mini-Projects

Welcome to the repository of the current mini-projects for the Machine Learning Engineering course. As you work through the curriculum, you will need to complete each mini-project and review and discuss them with your Mentor.

It is highly recommended to fork this repository on Github and share it with your Mentor so that they can easily follow your progress.  Here is an excellent resource that details how to do it: https://docs.github.com/en/github/getting-started-with-github/fork-a-repo

## Installation

Below are detailed instructions on how to get those mini-projects up and running. None of those projects should require tons of CPU or memory, so you are welcome to run those locally on your computer or through any hosted jupyter notebook services such as Deepnote or Google's Collab.

### Local

Now, to run those projects locally, we recommend you first install Anaconda for your operating system (Windows, Mac, Linux) by downloading it and following the instructions here: https://www.anaconda.com/products/individual#Downloads

Once Anaconda is installed, run the following command to create a dedicated python environment with all the libraries and packages needed to run all the mini projects in this repo:
```conda env create -f environment.yml```

Then activate the environment by running:
```conda activate mec-miniprojects```

Then create an ipython kernel for Jupyter based on this environment:
```python -m ipykernel install --user --name mec-miniprojects --display-name "Python (MEC Mini-Projects)"```

Finally, launch Jupyter Lab and navigate to each mini-project notebook and make sure to select the kernel that you created above:
```jupyter lab```

### Google Colab

It is straightforward to work and run the notebooks for each mini-project (that is, except mec-5.5.4-webscraping-project since it is not a notebook-style mini project)in Google Colab by leveraging the Github integration
Please note that you will need to have forked the mini-projects repository for this to work.

Here are the steps:
- Go to https://colab.research.google.com/ (and log in with a Google account)
- Select File -> Open Notebook
- Select the Github Tab in the popup window which opened
- Login with your Github account, and allow Google Colab to have read/write access to your private repositories
- Once the authorization is processed, you should now see a list of all your repositories on Github. All you need to do for this step is to select the forked mec-mini-projects repo
- Once the mec-mini-projects repo is selected, Colab will ask you which notebook you want to open in that repo. 
- After selecting the mini-project notebook of your choice, it will be open and ready to use

Once you are done working on your mini-project notebook in Colab, you can easily save a copy of your notebook back to Github by clicking on File -> Save a Copy To Github, and it will ask you to enter a commit message, a file name. It will then commit your changes and work to Github.

#### Cautionary words
While super easy to get up and running and an excellent environment for all the MEC mini-projects, Google Collab has one main drawback: python library versions. You can easily install packages, but Colab comes with a fleet of existing data science-related packages. They may not always be the same version expected in the various mini-projects. There can sometimes be incompatibilities, requiring you to install or upgrade some of the packages needed.

## Contributions & PRs welcome!

To provide the best possible learning content to our students, please do not hesitate to open Github issues or submit PRs if you catch any typos in those mini-projects.