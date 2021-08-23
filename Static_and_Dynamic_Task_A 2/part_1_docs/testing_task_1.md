### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #should be '==' instead of '='
      return True
    else #should have a colon after 'else'
      return False
   

  dif highest_card(self, card1 card2): #should be 'def' instead of 'dif', should ahve a comma between 'card1' and 'card2'
  if card1.value > card2.value: # block of code from line 28 - 31 should be indented
    return card #this should be 'card1' not 'card'
  else:
    return card2
  


def cards_total(self, cards):
  total # 'total has not been defined
  for card in cards:
    total += card.value
    return "You have a total of" + total # this line needs to be in line with the "for" on line 37, and not indented to be part of the for loop. This also needs to be changed to an f string to be able to combine int and str values.
  
```
