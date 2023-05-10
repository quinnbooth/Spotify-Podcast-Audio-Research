# The Effect of Audio Features on Podcast Performance

## Abstract
  Podcasts have popularized in recent years, but insufficient research
  has been conducted on them. With this study, we intend to identify
  which audio features affect a podcast's star rating and number of
  ratings. The particular audio features we examined are the fundamental
  frequency, jitter, shimmer, harmonics-to-noise ratio, and loudness of
  numerous shows in the official Spotify Podcasts Dataset. This dataset
  includes podcast metadata and openSMILE audio metrics which we
  compared to the equivalent Apple star ratings and numbers of ratings.
  To find significant relationships, we ran t-tests with
  Benjamini-Hochberg corrections to prevent false positives in our
  multivariate comparison. These statistical tests indicated a positive
  relationship between Harmonics-to-Noise Ratio (HNR) and number of
  ratings along with negative relationships between jitter and number of
  ratings as well as shimmer and number of ratings. These results will
  allow podcasters to optimize their audio in order to garner more user
  ratings and thus achieve more success.

## Authors
  **Quinn Booth**\
  Columbia University\
  `qab2004@columbia.edu`
  
  **Lara Karacasu**\
  Columbia University\
  `lk2859@columbia.edu`
 
## Introduction

### Research Questions

Pitch, volume, and speech rate affect the perceived confidence of a
speaker (Guyer et al., 2019). Louder podcasts tend towards higher
ratings (Shafiei et al., 2020) and there exists a positive relationship
between speech rate and popularity in music (Gauvin, 2017).
Additionally, we have seen -- especially in the case of fake news --
that overly confident and persuasive media is attractive to viewers.
Therefore, do podcasts with a more confident and persuasive tone perform
better upon release? Further, do the patterns in certain audio features
associated with confident speakers, such as pitch and volume, indicate
anything about a podcast's success?

Alternatively, some auditory features reflect audio quality. For
example, harmonics-to-noise ratio measures relative additive noise in a
signal, and it is a significant predictor of roughness in voice samples.
Jitter is associated with irregular vibrations in the vocal folds.
Finally, shimmer is a measure of variability in amplitude, correlated
with noise emission and breathiness (Bottalico et al., 2018). Previous
studies have also found a positive relationship between audio quality
and favorable perception of recordings and their speakers (Newman et
al., 2018). Thus, would podcasts with higher audio quality tend to
receive higher ratings and more engagement?

### Hypotheses

1.  Hypothesis 1: Podcasts with higher star ratings will differ
    significantly from podcasts with lower star ratings across multiple
    acoustic features.

2.  Hypothesis 2: Podcasts with larger numbers of ratings will differ
    significantly from podcasts with smaller numbers of ratings across
    multiple acoustic features.

3.  Hypothesis 3: Podcasts with higher star ratings and larger numbers
    of ratings will have significantly: lower fundamental frequency,
    less jitter, less shimmer, lower harmonics-to-noise ratio, and
    greater loudness.

### Previous Research

There exists little research on the audio characteristics of podcasts,
yet knowing which auditory qualities lead to favorable reception would
be a fantastic tool for aspiring creators. In this study, we choose to
explore the relationship between fundamental frequency, jitter, shimmer,
harmonics-to-noise ratio, and loudness in regards to the star ratings
and number of ratings that podcasting shows receive. Fundamental
frequency and volume are most basic characteristics of spoken audio,
making their discussion of great importance. Additionally, jitter,
shimmer, and harmonics-to-noise ratio are widely regarded as important
metrics of general audio quality. Fortunately, though little work has
been done on podcasts, many studies have discussed the relationship
between other forms of spoken audio and our perception of the
speaker/media.

First, there is an established relationship between lower vocal
registers and perceptions of power and credibility. An experiment in
this vein was conducted with 51 men and women who were instructed to
introduce themselves in a number of manners. When asked to emulate a
figure of authority, such as a doctor, subjects would subconsciously
lower their vocal register. Such findings indicated a relationship
between lower voices and power, authority, and trustworthiness
(Sorokowski et al., 2019). From a biological perspective, a compilation
of studies indicate that Old World monkeys likely developed this
association because of a preexisting connection between deep tones and
large objects/animals. We consistently associate lower voice pitches -
measured by fundamental frequency - with social status, leadership
status and, again, power (Aung et al., 2020). With these connections in
mind, it is likely that podcasts with a lower vocal register will give
an impression of credibility and authority.

Humans also associate a fast speaking rate with being confident. A study
had 394 undergraduate students rank audio recordings with
sped-up/slowed-down speech in terms of how confident they perceived the
speaker. The results showed that students thought faster speech rates
had more confident undertones (Guyer et al., 2019). In support, other
researchers synthesized the Trinity Speech-Gesture Dataset and had 35
online participants rank recordings on a scale of confidence. Subjects
consistently rated recordings with faster speech rates with higher
confidence levels (Kirkland et al., 2022). Therefore, in addition to
pitch, the speech rate in podcasts likely affects the hosts' perceived
confidence. While we are not directly examining speech rate, these
studies show how a particular audio feature can affect our perception of
a speaker.

Aside from pitch and speech rate, there is a relationship between
volume, dynamics (pausing) and engagement/ratings in -- specifically --
podcasts. A study similar to ours was run, searching for relationships
between Apple podcast average engagement and numerical ratings, and
designated auditory features: pausing, pitch range, participants,
intonation, and loudness. They ultimately found meaningful relationships
between total engagement and loudness as well as total engagement and
pausing, but no meaningful connections between any of the other
features. No relationship was found for numerical ratings with any of
the audio features, which could have been a result of the methodology:
the authors randomly sampled over all podcasts instead of randomly
sampling over each rating bucket to get a more even distribution (the
majority of podcasts are highly rated) (Shafiei et al., 2020).

As previously stated, audio quality metrics can also influence the
perception of not only the recording, but the perception of the speaker
in the recording. A 2018 study asked participants to evaluate identical
conference talks and radio interviews, differentiable only with respect
to audio quality. The recordings with lower audio quality were rated
significantly less favorably, and the content of those presentations
were rated as being less important in comparison their higher-quality
counterparts. Further, the speakers were evaluated as being less
intelligent and less likeable (Newman et al., 2018). Similarly, a 2014
study found that young female speakers with more vocal fry, a vocal
quality associated with higher shimmer and jitter (Kuang et al., 2016),
were perceived as significantly less likeable and less intelligent
(Anderson et al., 2014).

Power, trustworthiness, likeability, and confidence are facets of
persuasion: a characteristic of successful products. Perceived
confidence has a large bearing on the success of a persuasive attempt,
indicated in a study that showed how perceived competence affects
persuasiveness when speaking through an analysis of successful
Kickstarter campaigns (Wang et al., 2021). In other words, if we believe
someone is trustworthy, we are more easily persuaded, regardless of
their information's integrity. An affirmative study had subjects listen
to recordings of persuasive material, some with paralinguistic material:
an indicator of confidence. When shown recordings with more
paralinguistic material, subjects gave higher ratings of persuasiveness.
From these studies, we can see that persuasiveness greatly depends on
perceived competence and confidence, rather than solely the quality of
provided information (Zant et al., 2020). Take for example the growing
prominence of fake news. Fake news and propaganda use stability to be
persuasive and establish a sense of credibility (Vamanu, 2019). Under
the logical assumption that people support things that they believe in,
podcasts with more persuasive qualities should see greater success.
Given persuasiveness is reflected by confidence, podcasts with lower
fundamental frequency and greater loudness (characteristics of
confidence) should perform better, hence our hypotheses.

## Method

### Independent Variables

1.  **Fundamental Frequency**\
    F0semitoneFrom27.5Hz_sma3nz_amean openSMILE reading for a podcast's
    episodes, averaged.\
    \
    F0semitoneFrom27.5Hz_sma3nz_amean is the mean fundamental frequency
    measured on a logarithmic frequency scale beginning at 27.5 Hertz.
    This represents the lowest harmonic/frequency produced by an audio
    file.

2.  **Jitter**\
    jitterLocal_sma3nz_amean openSMILE reading for a podcast's episodes,
    averaged.\
    \
    jitterLocal_sma3nz_amean is the mean difference in period length of
    sequential fundamental frequency samples. Jitter is associated with
    irregular vibrations in the vocal folds. This can manifest in
    choppiness or roughness of the voice.

3.  **Shimmer**\
    shimmerLocaldB_sma3nz_amean openSMILE reading for a podcast's
    episodes, averaged.\
    \
    shimmerLocaldB_sma3nz_amean is the mean difference in amplitude of
    sequential fundamental frequency periods. More shimmer can make a
    voice sound breathy.

4.  **Harmonics-to-Noise Ratio**\
    HNRdBACF_sma3nz_amean openSMILE reading for a podcast's episodes,
    averaged.\
    \
    HNRdBACF_sma3nz_amean is the amount of noise which falls within a
    harmonic of the fundamental frequency versus that which does not.
    Harmonics-to-noise ratio measures relative additive noise in a
    signal. A lower harmonics-to-noise ratio indicates more noise in
    someone's voice, as opposed to harmonics, making it sound more
    coarse.

5.  **Loudness**\
    loudness_sma3_amean openSMILE reading for a podcast's episodes,
    averaged.\
    \
    loudness_sma3_amean is simply the average volume of audio/its
    signal's intensity.

### Dependent Variables

1.  **Star Rating**\
    Podcast rating out of five stars on Apple Podcasts.

2.  **Number of Ratings**\
    Number of ratings on Apple Podcasts.

In addition, we define podcasts with \"higher ratings\" as podcasts with
an average Apple star rating above the median rating, and podcasts with
\"lower ratings\" as podcasts with an average Apple star rating below
the median. Similarly, we define podcasts with \"higher engagement\" as
podcasts with a number of Apple ratings above the median number of
ratings, and podcasts with \"lower engagement\" as podcasts with a
number of Apple ratings below the median. In order to validate the
findings, we will also run our statistical testing using another, more
extreme, split point: the 90-10 split point. That is, our validation
tests consider ratings and engagement metrics at or above 90th
percentile as being high, while ratings and engagement metric at or
below the 10th percentile as being low.

### Data Collection

The majority of our research centered around data collection,
preparation, and aggregation. The relevant data from the Spotify
Podcasts Dataset is spread across multiple folders. Thus, we collected
the podcast metadata and openSMILE audio data from separate directories
and compiled it into our own contiguous dataset. Initially, we formatted
Spotify's metadata.tsv file, which contains basic information about
every English podcast episode in the shared Box. This required reading
the TSV into a Jupyter Notebook, grouping the entries by show name, and
conglomerating episodes per show into a listed field. Additionally, we
cleaned the data by removing any insignificant podcasts, as well as
podcasts with uncommon RSS feeds. We chose a minimum threshold of 30
episodes for this task: that is, podcasts with fewer than 30 episodes
were not included in our dataset. The reasoning behind this decision is
primarily that averaging audio features across a podcast with a
minuscule number of episodes may lead to skew in the final dataset, as
we would not be able to confidently use those means as representative
values for the podcast show as a whole. More broadly, larger samples
better approximate populations, and consequently yield tighter
confidence intervals. However, each podcast show also corresponds to one
observation in our dataset, and an extremely high threshold would thus
yield a low number of observations. Empirically, choosing a minimum
threshold of 30 episodes per podcast balanced both trade-offs:
ultimately, our final dataset contained 422 episodes.

An RSS feed is an XML file that stores links to and information
regarding a podcast's episode history. Removing shows with
uncommon/unreachable RSS feeds assists our RSS scraping algorithm. This
program reaches into RSS feeds that remain after our data is cleaned and
retrieves any dates associated with a show's episode list. We isolated
shows with sufficient online documentation using this method.
Originally, these dates were meant to interface with the Twitter API to
run sentiment analysis on Tweets advertising podcast episodes in our
dataset. Ultimately, we used the Apple ratings to assess a show's
performance and cross-referenced the dates from the RSS feeds against
the Apple ratings to guarantee validity. RSS feeds also helped us
determine our 30 episode threshold for shows we would allow into our
final CSV. Dipping much below 30 episodes resulted in numerous personal
or less used RSS feed formats entering our dataset, meaning we would
have to account for these in our RSS feed scraper. It was more feasible
for us to employ a threshold that would guarantee a smaller number of
popular RSS feed hosts.

After preparing the initial CSV, we incorporated the openSMILE data from
the Spotify Podcasts Dataset. openSMILE is able to extract 88 features
from an audio file; the creators of the Spotify dataset ran this
analysis on every available episode. This information was held in a
separate portion of the Box in a complicated folder structure, navigable
by the show's show filename prefix. Unfortunately, the files in this
portion of the Box were too large for us to download -- attempting to
ZIP the larger directories would result in a network error. Unable to
download the parent folders, the only possibility was to individually
download upwards of 400 specific smaller folders. Because performing
this task manually is infeasible during our time frame, we developed a
Selenium downloading interface. Using our login credentials, the
Python-based Selenium application logs into Box to access the Spotify
Podcasts Dataset. It uses our current CSV to construct a list of show
file prefix names with undownloaded openSMILE data and iterate through
the folder structure, downloading them one at a time. Note that we have
explicit permission to download and access this data.

With the openSMILE data collected, we wrote additional Python scripts to
take the averages of each auditory feature. Due to the complicated
Hierarchical Data Format of the openSMILE files, as well as the
multi-layered directory structure of the openSMILE folders themselves,
navigating to the appropriate file for a given podcast show, and
subsequently extracting the relevant audio data, was a nontrivial task.\
To better understand the HDF file structure, we used the HDFView
application, which was developed by the creators of the format itself
for decomposing HDF files. After visualizing and documenting the
internal structure of the HDF files, we wrote a Python script to extract
the 88 feature names. This script uses the h5py and pandas libraries for
traversing the openSMILE file objects, retrieving the feature names, and
adding them to our final CSV. We wrote a separate Python script to
iterate through the local directories containing HDF files, calculate
the mean of each auditory feature for a given episode, average these
means to obtain representative feature values for each show, and then
add these values to the appropriate columns in our CSV. We imported many
libraries for this task, including h5py, pandas, numpy, and pathlib.

Finally, we gathered performance metrics. Spotify does not have any
functionalities for rating or reacting to podcasts. As a result, we
looked to outside sources to add them into our dataset. Ultimately, we
chose Apple Podcasts. While a few other platforms do contain metrics for
podcast performance, many of them would have added confounds to the
experiment. For instance, YouTube Podcasts features video feed in
addition to the audio feed, which is likely to have a large competing
impact on user ratings and engagement. Apple Podcasts contains the audio
feed alone, and its interface is the most similar to that of Spotify
Podcasts. It has a five star rating system and publicizes how many users
have rated a show, giving valuable information about its reception. In
order to collect this data, we manually searched for each show in our
dataframe and input the average star rating, number of ratings, and show
genre. Scraping initially seemed like a good solution for this task, but
it quickly proved unworthy of the effort. Many shows exist with
duplicate names, or have changed their names since they were sampled in
the Spotify dataset, meaning that a set of human eyes was necessary to
preserve the integrity of the data. Therefore, we manually collected and
verified the rating metrics. Upon finishing this manual portion of data
collection, we removed podcasts from our CSV that didn't have an Apple
Podcasts page. This step concluded the data collection and integration
pipeline.

## Data

Our dataset includes information from a variety of sources, including
Spotify, RSS Feeds, openSMILE, and Apple Podcasts. Each row our compiled
CSV represents a unique podcast show (that has passed the constraints
and thresholds described in our Method section), and its columns
encompass the podcast's metadata and average auditory features. The
finalized dataset contains all metrics relevant to testing our
hypotheses: confirming that episodes with lower fundamental frequency,
less jitter, less shimmer, lower harmonics-to-noise ratio, and greater
loudness tend to receive more/better star ratings.

### Spotify Podcasts Dataset

We primarily used the Spotify Podcasts Dataset to conduct our research,
particularly its subset of English podcasts. The Spotify Podcasts
Dataset is a collection of over 100,000 English podcast episodes -- and
additionally many Portuguese podcasts we didn't explore -- hosted on
Spotify, containing transcripts, RSS feeds, show titles, show genres,
episode titles, and other associated metadata. From the information in
the Spotify Podcasts, we extracted the following data as metadata
features for our own dataset:

1.  **Show Name**

2.  **Episode Name**\
    A list of episode names associated with the show name.

3.  **Episode Date**\
    A list of episode dates, ordered such that they correspond to the
    episode names.

4.  **RSS Link**\
    Link to an XML file containing documentation of a podcast show's
    history of episodes, including descriptions, dates, and file
    download links.

5.  **Episode Duration**\
    A list of episode durations, ordered such that they correspond to
    the episode names. (Grabbed externally from RSS feeds)

6.  **Show Filename Prefix**\
    A unique sequence of alphanumeric characters used to identify the
    show.

7.  **Episode Filename Prefix**\
    A list of unique sequences of alphanumeric characters used for
    identifying episodes, ordered such that they correspond to the
    episode names.

Additionally, the Spotify Podcasts Dataset includes a separate folder
structure containing auditory data retrieved with the openSMILE audio
signal processing toolkit. Each file in the openSMILE folder stores
large amounts of numerical data using multidimensional arrays, via a
Hierarchical Data Format. There are 88 total auditory features sampled
for each episode, including our features of interest: fundamental
frequency, jitter, shimmer, harmonics-to-noise ratio, and loudness.
These features were sampled every 0.48 seconds, for each podcast episode
within our podcasts dataset. Hence, to create a representative value for
each podcast with respect to each feature, we averaged these samples by
feature before adding them to the aggregate dataset.

## Apple Podcasts Data

Although the Spotify Podcasts Dataset contains metadata and auditory
data, it lacks information on ratings and engagement. Spotify does not
allow users to rate, like or heart specific podcasts and any existing
engagement metrics are not readily available to the public. Hence, we
separately collected the performance data for each podcast show from the
Apple Podcasts website. This shouldn't create much of a disconnect in
our analysis, since we are only grabbing auditory features (our
independent variables) from Spotify; these auditory features should be
the same on the Apple Podcasts platform given they uploaded the same
audio files. From Apple Podcasts, we extracted the data as performance
features for our own dataset:

1.  **Link to Apple Podcast Page**

2.  **Average Star Rating**\
    The average star rating, a float of precision 1, given by podcast
    raters for a show.

3.  **Number of Ratings**\
    The number of distinct podcast ratings for a show.

4.  **Show Genre**

We matched the performance data to the larger dataset by podcast title,
podcast host, and dates. The Apple Podcasts performance metrics were
scraped between April 3rd and April 4th of 2023. Please note that future
attempts to grab these same metrics may result in different results, as
the metrics are dynamically updated.

## Results/evaluation

For our statistical analyses, we ran two-sample t-tests with
Benjamini-Hochberg correction to prevent false positives in our
multivariate comparison. We used two-sample t-tests in accordance with
our hypotheses, which only distinguish between low and high metrics. We
loaded our final dataset into RStudio and used the ttest() function to
obtain the p-values, and then called p.adjust() with method = \"BH\" for
our corrections. We use a significance level alpha of 0.01. All p-values
displayed in tables are Benjamini-Hochberg corrected.

### Hypothesis 1

Podcasts with higher star ratings will differ significantly from
podcasts with lower star ratings across multiple acoustic features.

To test Hypothesis 1, we ran two-sample two-tailed t-tests for each of
our five audio features. In Test 1, the two populations being tested
were podcasts with star ratings above the median and those with ratings
below the median. We aimed to determine if there was a true difference
in the two populations' means with respect to each feature. Because
setting the cut-off point for the two separate populations at the median
is somewhat arbitrary, we also performed another set of t-tests for each
hypothesis to validate our results. Thus, Test 2 uses the 10th
percentile as the cut-off point for podcasts with a \"low\" average star
rating, and it uses the 90th percentile as the cut-off point for
podcasts with a \"high\" average star rating. Thus, if both Test 1 and
Test 2 yield significant results for the same acoustic feature, we
conclude that podcasts with higher star ratings do differ significantly
from podcasts with lower star ratings across that feature.

**Table 1: P-values for hypothesis 1**

|   Variable   | Test 1 | Test 2 |
|--------------|--------|--------|
| F. Frequency | $0.789$  | $0.962$  |
| Jitter       | $0.474$  | $0.962$  |
| Shimmer      | $0.486$  | $0.962$  |
| HNR    | $0.947$  | $0.962$  |
| Loudness     | $0.423$  | $0.962$  |

Table 1 displays the p-value for all t-tests conducted for Hypothesis 1.
Evidently, none of the alpha values obtained for any t-test conducted
for Hypothesis 1 were below the confidence level of 0.01. Thus, we
conclude that there is no true statistical difference in feature means
between podcasts with higher star ratings and podcasts with lower star
ratings for any of the five acoustic features tested.

### Hypothesis 2

Podcasts with larger numbers of ratings will differ significantly from
podcasts with smaller numbers of ratings across multiple acoustic
features.

To test Hypothesis 2, we ran two-sample two-tailed t-tests for each of
our five audio features. In Test 1, the two populations being tested
were podcasts with more ratings than the median and those with fewer
ratings than the median. We aimed to determine if there was a true
difference in the two populations' means with respect to each feature.
Again, we used a second set of t-tests to validate the results. Thus,
Test 2 uses the 10th percentile as the cut-off point for podcasts with a
\"low\" number of star ratings, and it uses the 90th percentile as the
cut-off point for podcasts with a \"high\" number of star ratings. Thus,
if both Test 1 and Test 2 yield significant results for the same
acoustic feature, we conclude that podcasts with more ratings do differ
significantly from podcasts with fewer ratings across that feature.

**Table 2: P-values for hypothesis 2**

|   Variable   | Test 1 | Test 2 |
|--------------|--------|--------|
| F. Frequency | $0.024$  | $0.102$  |
| Jitter       | $0.003*$ | $0.007*$ |
| Shimmer      | $0.012$  | $0.003*$ |
| HNR    | $0.005*$ | $<0.001*$|
| Loudness     | $0.405$  | $0.545$  |

Table 2 displays the p-value for all t-tests conducted for Hypothesis 2.
Evidently, the jitter and harmonics-to-noise ratio features passed both
Test 1 and Test 2, the shimmer feature passed Test 2 only, and
fundamental frequency and loudness failed both tests. Hence, we conclude
that there is no true statistical difference in feature means between
podcasts with higher star ratings and podcasts with lower star ratings
for fundamental frequency, shimmer, and loudness. However, there is
sufficient evidence to show that podcasts with more ratings do differ
significantly from podcasts with fewer ratings across two acoustic
features: jitter and harmonics-to-noise ratio. Thus, Hypothesis 2 was
supported.

Figures 1 and 2 display means of jitter and harmonics-to-noise ratio.
The high number of ratings population is in red; low number of ratings,
blue. Looking towards the error bars, there is no overlap, indicating a
significant difference in the means.

![A barplot plotting the means of jitter against rating
population.](j_barplot.png){#fig:galaxy width="7.5cm"}

![A barplot plotting the means of HNR against rating
population.](hnr_barplot.png){#fig:galaxy width="7.5cm"}

### Hypothesis 3

Hypothesis 3: Podcasts with higher star ratings and larger numbers of
ratings will have significantly: lower fundamental frequency, less
jitter, less shimmer, lower harmonics-to-noise ratio, and greater
loudness.

To test Hypothesis 3, we ran two-sample one-tailed t-tests for each of
our five audio features. For each audio feature, we ran four t-tests.
Because this hypothesis makes claims about both podcast star ratings and
the number of ratings, as opposed to just one of those two metrics,
there are four total populations: (1) podcasts with higher star ratings,
(2) podcasts with lower star ratings, (3) podcasts with higher numbers
of ratings, and (4) podcasts with lower numbers of ratings. Populations
1 and 2 are mutually exclusive as well as populations 3 and 4. Note that
populations 1 and 2 are not mutually exclusive from populations 3 and 4.
As with the previous hypothesis, podcasts with star ratings below the
median are considered to have low ratings, podcasts with fewer ratings
than the median number of ratings are considered to have low engagement,
and so on. We aimed to determine if there was a true difference between
the high and low star ratings populations in the hypothesized
directions, as well as a true difference between the high and low
engagement populations in the hypothesized directions.

Again, we employ an alternative set of t-tests for validation of
results. Test 1 and Test 3 both use the median as the boundary between
high and low. Similarly, Test 2 and 4 are both use the 10th percentile
as the upper boundary for low and the 90th percentile as the lower
boundary for high. Test 1 and 2 use the \"lesser\" directionality and
Test 3 and 4 use the \"greater\" directionality as parameters for the
one-tailed tests. We performed separate one-tailed t-tests with
different critical regions (both less and greater) in order to verify
the observed directionality.

**Table 3: Ratings vs. Audio Features**

|   Variable   | Test 1 | Test 2 |
|--------------|--------|--------|
| F. Frequency | $0.999$  | $0.999$  |
| Jitter       | $0.002*$ | $0.005*$ |
| Shimmer      | $0.009*$ | $0.003*$ |
| HNR          | $0.999$  | $0.999$  |
| Loudness     | $0.999$  | $0.999$  |
|   Variable   | Test 3 | Test 4 |
|--------------|--------|--------|
| F. Frequency | $0.024$  | $0.102$  |
| Jitter       | $0.999$  | $0.999$  |
| Shimmer      | $0.999$  | $0.999$  |
| Harmonics    | $0.005*$ | $<0.001*$|
| Loudness     | $0.337$  | $0.455$  |

**Table 4: Stars vs. Audio Features**

|   Variable   | Test 1 | Test 2 |
|--------------|--------|--------|
| F. Frequency | $0.958$  | $0.788$  |
| Jitter       | $0.958$  | $0.788$  |
| Shimmer      | $0.958$  | $0.788$  |
| Harmonics    | $0.958$  | $0.788$  |
| Loudness     | $0.958$  | $0.788$  |

Table 3 displays the results of Test 1, Test 2, Test 3, and Test 4 for
the number of ratings variable. Table 4 displays the results of the same
tests for the average star rating variable. Note that, for a given
table, a feature should only pass either Test 1 and Test 2, or Test 3
and Test 4, but not both. A feature which passes more than two tests
would indicate a negative result, as it would fail to adhere to the
hypothesized directionality.

Hypothesis 3 was partially supported. Based on Table 4, we found no
significant relationships between any of the audio features and average
star rating. However, Table 3 yielded several significant findings. The
jitter and shimmer features passed both Test 1 and Test 2, the
harmonics-to-noise ratio feature passed both Test 3 and Test 4, and all
other tests failed. Thus, podcasts with more ratings tend to have less
jitter, less shimmer, and a greater harmonics-to-noise ratio than
podcasts with fewer ratings.

Figures 3 through 7 are scatterplots plotting each audio feature against
the number of ratings. We plotted regression lines on top of the
scatterplot to show the overall association between the variables:
positive, negative, or no association. Note that the association between
the variables themselves is not strictly linear; the lines are only
meant to show the directionality of the relationship, if one exists.
Specifically, we note that the number of ratings decreases with
increased jitter and shimmer, and the number of ratings increases with
increased harmonics-to-noise ratio. The fundamental frequency and
loudness plots do not capture any significant relationship, but they are
included for completeness.

![A scatterplot plotting fundamental frequency against number of
ratings.](ff_sc.png){#fig:galaxy width="7.5cm"}

![A scatterplot plotting jitter against number of
ratings.](j_sc.png){#fig:galaxy width="7.5cm"}

![A scatterplot plotting shimmer against number of
ratings.](sh_sc.png){#fig:galaxy width="7.5cm"}

![A scatterplot plotting harmonics-to-noise ratio against number of
ratings.](hnr_sc.png){#fig:galaxy width="7.5cm"}

![A scatterplot plotting loudness against number of
ratings.](l_sc.png){#fig:galaxy width="7.5cm"}

## Conclusion

Our study of the Spotify Podcasts Dataset indicates that there is a
significant difference in multiple audio features (jitter and
harmonics-to-noise ratio) between podcasts with larger numbers of
ratings and smaller numbers of ratings, supporting our second
hypothesis. It also shows a significant negative relationship between
both jitter and number of ratings, and shimmer and number of ratings,
along with a significant positive relationship between
harmonics-to-noise ratio and number of ratings. This finding partially
supports our third hypothesis. We found no significance in any of our
comparisons between podcasts with high star ratings and low star
ratings, along with no significance for the fundamental frequency and
loudness audio features with either star ratings or number of ratings.

Limitations of our dataset include the differences between Apple
Podcasts and Spotify data and the skewed star rating metric. One issue
with the design of our study is the disconnect between the Spotify
Podcasts Dataset audio features and Apple Podcasts rating information.
This was unavoidable given the absence of ranking features on the
Spotify platform; users are able to like songs, but there is no
equivalent for podcasts. Though this detachment isn't ideal, Spotify and
Apple Podcasts both pull podcast information from the same RSS feeds,
including their audio files. Therefore, the audio metrics should be
uniform across the two platforms. We believe that this continuity
minimized any associated error in our dataset. Additionally, since
rating information was not included in the Spotify dataset during the
time of its collection, we were only able to sample it for ourselves in
the current day. The Spotify Podcasts Dataset was taken in 2019 and
2020, making it slightly outdated. We attempt to control for this by
taking averages of the shows' audio metrics, measuring the general
tendencies of a show rather than the granular episode-by-episode
features that are more subject to variation. Still, this time disconnect
could lead to discrepancies in our results. Finally, the data on star
ratings that we pulled from Apple Podcasts is extremely skewed towards 5
stars. Figure 8 exemplifies this skew and also a breakdown of podcast
genre in our dataset. Because there is little variance in star ratings,
we found no significance in any of our hypotheses regarding them. One
possible solution could have been to bucket podcasts with number of
stars and then sample from each bucket. However, we could not pursue
this avenue because very few samples had star ratings below 4 stars,
meaning that the sample size would any subsequent analysis would be
insufficient.

The findings of this study have direct application in the emerging field
of podcasts. Knowing that podcast shows with minimal jitter and shimmer
and greater harmonics-to-noise ratios tend to garner more ratings is a
powerful tool for up-and-coming creators to optimize their audio for
success.

![A stacked barplot displaying star ratings by
genre](star_ratings.png){#fig:galaxy width="7.5cm"}

## Future work

To build on this research, one could examine alternative sources for
assessing the performance of a podcast. We ultimately decided to analyze
the Apple Podcast ratings, but had originally planned to use the
Twitters of podcasts, grabbing metrics from any Tweets advertising their
episodes. By using an alternative source for rating metrics, one could
gather more targeted measurements of performance, including items such
as likes, comments, views (and retweets if using Twitter). Comments
could be valuable for sentiment analysis, to determine how the viewers
felt when listening to an episode or show. Apple Podcasts also has
comments associated with their five star ranking system which could be
analyzed for sentiment.

Additionally, many podcasts come with an accompanying video. We looked
at podcasts in an exclusively auditory context, but there's much to be
said regarding platforms such as YouTube where creators interview
celebrities live in front of the camera, or have a long winded
conversation with friends that an audience can visually participate in.
Analyzing what qualities of video lead to better star ratings and more
ratings could be a unique extension of our work.

There also seems to be a relationship between the sentiment of audio and
its reception. In early psychology studies, acoustic features were not
reliable predictors of music popularity, while lyrical features were
slightly effective. Researchers found that chroma --- a measure of
melody and mood --- was a statistically significant predictor of music
popularity in 20.8 percent of cases (Lee and Lee, 2018). Another study
was conducted, again focusing on music popularity, where a strong
connection between main tempo and popularity was found. Popularity was
defined by the ranking of a given song in the Billboard Hot 100 music
charts (Gauvin, 2017). Random forests have also been used in order to
predict song popularity. Ultimately, more successful songs --- defined
as the songs that appeared on the Billboard Top 100 chart in the near
past --- tend to be 'happier' and more 'party-like' (Interiano et al.,
2018). This finding imply that a positive valence and strong energy
component might contribute to podcast success.

Given these findings, there's significant potential for a link between
sentiment and podcast performance, which future studies could explore.
Similarly, genre could be further explored as a potential indicator of
podcast performance. Future studies analyzing podcast performance, even
with respect to audio features, could separate show genres from one
another in order to further validate our results. Ultimately, many new
avenues exist for research in the podcast industry.

## Responsibilities

Both partners contributed an equal amount of work, and both partners
worked on every portion of the project. For the paper, project proposal,
and presentation slides, we each revised every paragraph individually
multiple times and therefore it would be too difficult for us to
separate them. We will list each partner's major responsibilities below.

1.  **Quinn:** Getting publication dates from RSS feeds and refining CSV
    (refine_csv.ipynb), iterating Selenium web scraper through folder
    tree structure and downloading files (opensmile_folder_finder.py),
    additional t-testing with 90-10 percentile populations and python
    verification of results (statistical_testing.Rmd), presentation
    (slides and in person), writing paper.

2.  **Lara:** Programming initial Selenium web scraper login and
    navigation mechanisms (opensmile_folder_finder.py), retrieving and
    processing openSMILE audio features from H5 files using Python
    (extract_audio_data.py, extract_opensmile_features.py), writing
    documentation for HDF format and software, performing statistical
    testing in R and creating visualizations (statistical_testing.Rmd),
    making slides for presentation, writing paper.

 

## References

Alex Zant, Jonah Berger. 2020. [How the voice
persuades](https://doi.org/10.1037/pspi0000193). *Journal of Personality
and Social Psychology*, 118(4), 661--682.\
Ambika Kirkland, Harm Lameris, Eva Szekely, Joakim Gustafson. 2022.
[Where's the uh, hesitation? The interplay between filled pause
location, speech rate and fundamental frequency in perception of
confidence](https://www.speech.kth.se/~jocke/publications/interspeech_2022.pdf).
*KTH Royal Institute of Technology*, 1-5.\
Ann Clifton, Sravana Reddy, Yongze Yu, Aasish Pappu, Rezvaneh Rezapour,
Hamed Bonab, Maria Eskevich, Gareth Jones, Jussi Karlgren, Ben
Carterette, and Rosie Jones. 2020. [100,000 Podcasts: A Spoken English
Document
Corpus](https://www.aclweb.org/anthology/2020.coling-main.519/).
*COLING*.\
Edgar Tanaka, Ann Clifton, Joana Correia, Sharmistha Jat, Rosie Jones,
Jussi Karlgren, Winstead Zhu. 2022. [Cem Mil Podcasts: A Spoken
Portuguese Document Corpus](https://arxiv.org/abs/2209.11871). *Arxiv*.\
Eryn J. Newman, Borbert Schwarz, et al. 2018. [Good Sound, Good
Research: How Audio Quality Influences Perceptions of the Research and
Researcher](https://journals.sagepub.com/doi/full/10.1177/1075547018759345).
*Science Communication*, 40(2): 246-257.\
Hossein Shafiei, Ahmad Khonsari, et al. 2020. [The Tongue Can Paint:
Understanding Popularity in Podcasting
Societies](https://doi.org/10.1145/3366424.3382712). *Companion
Proceedings of the Web Conference*.\
Hubert Léveillé Gauvin. 2017. [Drawing listener attention in popular
music: Testing Five musical features arising from the theory of
attention economy](https://doi.org/10.1177/1029864917698010). *Musicae
Scientiae*, 22(3): 291--304.\
Iulian Vamanu. 2019. [Fake News and Propaganda: A Critical Discourse
Research Perspective](https://doi.org/10.1515/opis-2019-0014). *Open
Information Science*, 3(1):197-208.\
Jianjing Kuang, Mark Liberman. 2016. [The effect of vocal fry on pitch
perception](http://languagelog.ldc.upenn.edu/myl/KuangICASSP2016.pdf).
*IEEE*.\
Joshua Guyer, Leandre Fabrigar, Thomas Vaughan-Johnston. 2019. [Speech
Rate, Intonation, and Pitch: Investigating the Bias and Cue Effects of
Vocal Confidence on
Persuasion](https://doi.org/10.1177/0146167218787805). *Personality and
Social Psychology Bulletin*, 45(3):389--405.\
Junghyuk Lee and Jong-Seok Lee. 2018. [Music popularity: Metrics,
Characteristics, and Audio-based
prediction](https://doi.org/10.1109/tmm.2018.2820903). *IEEE
Transactions on Multimedia*, 20(11):3173--3182.\
Longqi Yang, Yu Wang, et al. 2019. [More than Just Words: Modeling
Non-textual Characteristics of
Podcasts](https://doi.org/10.1145/3289600.3290993). *Proceedings of the
Twelfth ACM International Conference on Web Search and Data Mining*.\
Mario Corrales-Astorgano, David Escudero-Mancebo, César
González-Ferreras. 2018. [Acoustic characterization and perceptual
analysis of the relative importance of prosody in speech of people with
Down syndrome](https://doi.org/10.1016/j.specom.2018.03.006). *Speech
Communication*, 99:90-100.\
Myra Interiano, Kamyar Kazemi, et al. 2018. [Musical trends and
predictability of success in contemporary songs in and out of the top
charts](https://doi.org/10.1098/rsos.171274). *Royal Society Open
Science*, 5(5), page 171274.\
Pasquale Bottalico, Juliana Codino, et al. 2018. [Reproducibility of
Voice Parameters: The Effect of Room Acoustics and
Microphones](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6529301/).
*Journal of Voice*, 34(3):320-334.\
Piotr Sorokowski, David Puts, et al. 2019. [Voice of Authority:
Professionals Lower Their Vocal Frequencies When Giving Expert
Advice](https://doi.org/10.1007/s10919-019-00307-0). *J Nonverbal Behav*
43: 257--269.\
Rindy C. Anderson, Casey A. Klofsta, et al. 2014. [Vocal Fry May
Undermine the Success of Young Women in the Labor
Market](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4037169/). *PLoS
One*, 9(5).\
Toe Aung, David Puts. 2020. [Voice pitch: a window into the
communication of social
power](https://doi.org/10.1016/j.copsyc.2019.07.028). *Current Opinion
in Psychology*, 30:154-161.\
Xin (Shane) Wang, Shijie Lu, X I Li, Mansur Khamitov, Neil Bendle. 2021.
[Audio Mining: The Role of Vocal Tone in
Persuasion](https://doi.org/10.1093/jcr/ucab012). *Journal of Consumer
Research*, 48(2):189--211.\
