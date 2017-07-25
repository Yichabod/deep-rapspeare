# Deep-Rapspeare
Synthesising Rap-inflected Shakespeare using an LSTM Recurrent Neural Network inspired by Karpathy

### Introduction - Preparing the training data — modifying the existing Character RNN - Lo and behold!  

*MOTH. But do check it out your soul (May more) D on this boy.* - a brief snippet of the final result.

#### Introduction
I was inspired by Andrej Karpathy's [post](http://karpathy.github.io/2015/05/21/rnn-effectiveness/), as well as seeing some other implementations of RNNs for text prediction to do something that combined both Shakespeare and the most popular current rappers.

#### Preparing the training data

I downloaded the complete works of Shakespeare from [Project Gutenberg](http://www.gutenberg.org/ebooks/author/65), and scraped the lyrics online. I here feel obliged to give a brief disclaimer: I'm not entirely clear on the legality of scraping metrolyrics' content, and, while I do know cases in the past where people have gotten in trouble (the [unfortunate Mr Swartz](https://www.wikiwand.com/en/United_States_v._Swartz) comes to mind), I don't think any harmful intention/ profit motives can be seriously argued, not to mention the fact that these lyrics sites don't even own the content they display.

  I haven't provided the code for scraping (As my father would always say, "You're either paranoid or you're stupid"), but it shouldn't be too big a challenge to flick through the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) documentation and/or look at some [existing implementations](https://github.com/mjbright/Scraper).
  I wrote a simple script (mixer.py) to alternate lines between the Shakespeare text and the Rap lyrics so that the RNN would be trained evenly on both texts, and because the sentence is the smallest unit of expression that preserves coherent syntax and ideas. If you had, say, alternated words between rap and Shakespeare, the result would be an uninteresting jumble of words with none of the distinct syntax that inflects either rap or Shakespeare.
  
#### modifying the existing Character RNN
  The character RNN I used was a Karpathy-inspired LSTM project [I found on Github](https://github.com/keskarnitish/Lasagne/blob/master/examples/lstm_text_generation.py) using Lasagne and Theano. In trying to to implement this code, however, I had to change a few things. 
  First was the fact that this model didn't actually save any weights, so I added save_weights(), which lets you save the results of training to pass to your friends so they could have some great Rapspeare fun without an expensive GPU.
  Second, I reduced the number of total Epochs to 30 from 50, because I was noticing no real improvement after 20 or so Epochs (Like those kids that peak in high school, I saw that Rapspeare pretty much reached its potential under the design architecture that I'd chosen, so I decided to pull the plug there). Not to mention the fact that it was hurting my wallet a little bit under the p2 GPU server I was paying for per GB-hour. 
  I made some other smaller modifications (adding print() messages etc), but unfortunately did not get around to restructuring the whole thing. If you look at Rapspeare, you'll see that many of the functions are contained within a big *main(num_epochs=NUM_EPOCHS)* function. This isn't the best practice as it stops you from calling the functions within *main()* individually to test/ modify, but at the time I was scared of toppling the precarious architecture around which I'd built RNN (It was a serious surprise/miracle to me that it worked at the time, in fact), and so sailing (I felt) between Charybdus and Scylla, I let the dormant beast that was Rapspeare lie, unperturbed (excuse the mongrel metaphors).
  
#### Behold!
*"And Lo, for the Earth was empty of Form, and void. And Darkness was all over the Face of the Deep. And We said: 'Look at that fucker Dance." - David Foster Wallace*

  At last, after hours of brain-hurting debugging, reading documentation, and wondering why I was so stupid, a brief light appeared at the edge of my computer screen, and a voice said, *"Straight out the fuckin Dungeons of Rap, Pac put your boys get they were/ 'Bustin' like a pussy shooterstandin Flashflook, I am dressed Emilems."*
  The asyndeton in the first sentence, with 'Pac put your boys get they were', really evokes a sense of disorientation and hurry. You get the sense that the speaker is trying to escape from some abominable force and is perhaps senile (with Alzheimer's?). The portmanteau in the second line, 'shooterstandin', carries forth this feeling of unbelievable hurry, and, by my estimation, could be a poem in and of itself. Contemporary poets have done worse (see [Aram Samoyam](https://www.wikiwand.com/en/Aram_Saroyan) if you want to know what I mean).
  But this incredible feat of wordsmithing didn't come about suddenly. The first few iterations were a little less pretty.
  
  
  
  As it turns out, this design decision had major implications with the complexity of the output that this RNN could produce. As you'll see later, Rapspeare_muse.py, or just Rapspeare, is able to generate  
