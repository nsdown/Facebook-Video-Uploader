# Facebook-Video-Uploader
This is a simple Python 2.7 script that uses Facebook's Graph Video API to upload videos to Facebook with dedupe functionality via sqlite and PeeWee. 

This script is really intended to be used in a digital publishing environment wherein video and their assoiated metadata need to be uploaded to a brand Facebook page in an automated fashion via cron job (i.e. this is really a server-side script). 

In order to really use Facebook's Graph Video API effectively, you need to simplfy the oAuth process. I strongly advise that you obtain permanent page access tokens by following these steps: 

http://stackoverflow.com/questions/17197970/facebook-permanent-page-access-token



