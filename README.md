# [Bakai Mitai meme]((https://knowyourmeme.com/memes/dame-da-ne-baka-mitai)) generator using First Order Motion Model

## pre-requirements
* python >=3.6
* pip
* ffmpeg
* download data (move all to `./data`):
	* [pre-trained weights](https://mega.nz/file/4cAyTIpT#5c5n43cLo4xc_uSgyBMIxMLB1S3_tNtzeiEZALnIyyc)
	* \[optional\] [pre-trained adversary weights](https://mega.nz/file/MNJw3ASA#ykp34kcenxKAEoTAW6__UhSrkxdchzqBq2p6qSzCkLE)
	* [video template](https://www.kapwing.com/videos/5f2831922695a400156ada1e) (save as `template.mp4` inside the `data` folder)
	* [audio template](https://filebin.net/tqtq7j5mvxq3j72k/dame.mp3?t=za5niv86)

## instalation

```shell
pip install -r requirements.txt
```

## usage
```shell
./main.py [image path]
```
results will be saved in the folder `./results`

# acknowledgements
thanks to [mohammedri](https://github.com/mohammedri) for his awesome [First Order Motion Model repo](https://github.com/AliaksandrSiarohin/first-order-model/blob/master/LICENSE.md)
