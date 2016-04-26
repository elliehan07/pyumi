pyumi 
======
![alt text][logo] 

pyumi is a python and IronPython package for automating and processing in umi simulations and visualization respectively. pyumi enables asynchronous simulation for urban energy modeling, meaning using pyumi a urban modeler can set a range of variables and a timer for set-and-forget simulations. 

1. selects buildings 
2. programmatically changes variables 
3. runs simulation 
4. saves simulation 
5. repeat 

In addition to asynchronous simulation, pyumi has a library for visualizing results from multiple files using matplotlib and panda's data frames.  (see vis.py) 

## Installation

To get started, download and unzip to your machine. 

![alt text][download] 


## Usage

Considering the user has some experience with umi, [if not check this out.] (http://www.urbanmodeling.net) 

1. Rhino Command : EditPythonScript to bring up the Rhino Python Editor 
2. Open "pyumi_rhino.py" from the downloaded file.
3. Scroll down to the hello world test code. 

```pyhton
	### Hello World ## 
	bldgs = GetBldgs()
	SetWWR(bldgs,0.9)
```

4. Run the code by hitting the play button on the Rhino Python Editor,  if all is right in the umiverse your builds should all change to 90% Window-Wall-Ratio. 

5. If not message me on github or post an issue to this repo. 
6. If it did work use the functions above to make your own simulation recipe.

Example:

```pyhton
	path = "C:\\Users\\YourUserName\\Desktop\\"

	bldgs = GetBldgs()

	for i in range(1,19):
    	name = i
    	i = i*0.025
    	SetWWR(bldgs,i)
    	for W in xrange(5):
	    	Rhino.RhinoApp.SetCommandPrompt(str(W))
	    	time.sleep(1)
    	rs.Command("_-UmiSimulateEnergy"+ " ")
    	## Wait time for simulation 50 seconds - Run a sim first to find out how long your model takes ##
    	for F in xrange(50):
	    	Rhino.RhinoApp.SetCommandPrompt(str(F))
	    	time.sleep(1)
    	Save(path+str(name))

```

## Contributing

If you would like to contribute your modification or code. 

1. Create a new branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`


## History
TODO: Write history

## Credits
TODO: Write credits
## License
TODO: Write license

## Dependencies for vis  
[Pandas] (http://pandas.pydata.org/ "Title")
[Matplotlib] (http://matplotlib.org/ "Title") 


[download]: https://github.com/jamiefarrell/pyumi/blob/master/img/DownloadZIP.PNG
[logo]: https://github.com/jamiefarrell/pyumi/blob/master/img/pyumi.png
