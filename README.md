# Generate text image
Generating an image of words in a given string using wordcloud module.

## How to run
- Clone the repo using `git clone https://github.com/mohdsaqibhbi/Generate_text_image.git`.
- Go to this directory using `cd Generate_text_image`
- Create virtual environment.
- Install dependencies using `pip3 install -r requirements.txt`.
- Generate an image of MCU characters with black background using 

`python generate_text_image.py -ws "Iron man,Thanos,Doctor Strange,Captain Marvel,Hulk,Vision,Thor,Groot,Rocket,Winter Soldier,Hela,Spiderman,Black Panther,Ultron,Wanda,Gamora,Star Lord,War Machine,Silver Quick,Mantis,Captain America,Loki,Antman,Black Widow,Hawkeye,Falcon,Drax,Shuri" -o output/mcu.png`
![mcu_black](https://github.com/mohdsaqibhbi/Generate_text_image/blob/master/output/mcu_black.png)

- Generate an image of MCU characters with white background using 

`python generate_text_image.py -ws "Iron man,Thanos,Doctor Strange,Captain Marvel,Hulk,Vision,Thor,Groot,Rocket,Winter Soldier,Hela,Spiderman,Black Panther,Ultron,Wanda,Gamora,Star Lord,War Machine,Silver Quick,Mantis,Captain America,Loki,Antman,Black Widow,Hawkeye,Falcon,Drax,Shuri" -o output/mcu_white.png -l white`
![mcu_white](https://github.com/mohdsaqibhbi/Generate_text_image/blob/master/output/mcu_white.png)

## Command line arguments

| tag (* = required)| variable          | options                                        | default value   |
|:-----------------:|:------------------|:-----------------------------------------------|:----------------|
| -ws *             | word_string       | string of words separated by comma             | REQUIRED        |
| -o *              | out               | path to output image                           | REQUIRED        |
| -l                | layout_color      | choices=["black", "white"]                     | "black"         |
| -W                | width             | width of image                                 | 1200            |
| -H                | height            | height of image                                | 800             |
| -s                | step_size         | difference between freqencies of words         | 50              |
| -b                | bias              | lowest initial frequency of a word             | 10              |
