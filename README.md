# delete_your_tweets

Recently, The Guardian encouraged their journalists to "regularly delete historical tweets". Read a digest at [Nieman's Lab](https://www.niemanlab.org/2022/05/think-carefully-before-you-quote-tweet-the-guardian-releases-new-social-media-guidelines-for-staff/).

Here is a repo to guide you in this task.

You would first need to get rights to use the Twitter API and download your Twitter archive. Then, in the archive file, find the tweet.js file and make it an JSON file replacing the first line...

```javascript
   window.YTD.tweet.part0 = [ {
```

and replace it with

```javascript
   {"data": [ {
```

... and for last line you need to add an extra "}" to make it a JSON object. Your file's last line will look like this:

```javascript
  } ]}
```

Feel free to give me your feedback.

I found that solution [here](https://dev.to/3zadessg/deleting-old-tweets-using-python-twitter-api-for-a-date-range-1a23).
