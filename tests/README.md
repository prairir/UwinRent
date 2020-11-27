# Running Automated Tests
The instructions below are for UNIX based OS's.

One of these tests uses the `Selenium` library which in this case uses the gecko web driver  and therefore requires the user to have Firefox installed beforehand. You can download Firefox [here](https://www.mozilla.org/ "here").

## Installing Gecko Web Driver
1. From `<MAIN>`, run the bash script to install. This will ask for your `sudo` password since the web driver needs to be moved to `/usr/local/bin`.

	run `bash ./tests/installGeckoDriver.bash`

Once installed the web driver does not need to be reinstalled on every run.

## Running Tests
To run these tests make sure the you have the server running according to the instructions in `<MAIN>`

1. Change directory into `<MAIN>/tests`

	run `cd ./tests`

* Create venv(optional but recommended for dev)

	* Create venv directory `<MAIN>/server/venv`

	run `mkdir ./venv`

	* Create venv 

		run `python3 -m venv ./venv/`

	* Activate venv 

	run `source ./venv/bin/activate`

2. Install the dependencies

	run `pip3 install -r requirements.txt`

3. Run the tests

	run `python3 -m pytest`
