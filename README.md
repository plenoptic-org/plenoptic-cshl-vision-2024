# plenoptic-cshl-vision-2024

Material for presentation at Cold Spring Harbor vision course, 2024. See the website for more details.


## Binder

The binder setup is the same as previous workshop tutorials I've put together but note that, when we had many users, the binder instance was freezing. I believe that was due to ffmpeg grabbing all the threads on the node and, since there were many users on the node ... that was bad. See [issue for discussion](https://github.com/plenoptic-org/plenoptic/issues/268), but I believe the solution is to add

``` python
plt.rcParams['animation.html'] = 'html5'
# use single-threaded ffmpeg for animation writer
plt.rcParams['animation.writer'] = 'ffmpeg'
plt.rcParams['animation.ffmpeg_args'] = ['-threads', '1']
```

to the top of the notebook.
