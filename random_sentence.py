import random

#wrote the below code in my first year of python programming :)
#will make new random sentence engine later

def SentenceNow():
    pt1=random.randint(1,10)
    pt2=random.randint(1,10) 
    pt3=random.randint(1,10)
    pt4=random.randint(1,10)
    tex=""
    tex2=""
    tex3=""
    if pt1==1:
        tex="In Conclusion,"
    elif pt1==2:
        tex="And So,"
    elif pt1==3:
        tex="Sometimes,"
    elif pt1==4:
        tex="Only when"
    elif pt1==5:
        tex="However,"
    elif pt1==6:
        tex="Almost monthly,"
    elif pt1==7:
        tex="Every Day,"
    elif pt1==8:
        tex="In the end,"
    elif pt1==9:
        tex="And then"
    elif pt1==10:
        tex="Afterwords,"
    if pt2==1:
        person=random.randint(1,3)
        if person==1:
            pstr="president"
        if person==2:
            pstr="governor"
        if person==3:
            pstr="senator"
        tex2=" the "+str(pstr)
    elif pt2==2:
        person=random.randint(1,5)
        if person==1:
            pstr="mailman"
        if person==2:
            pstr="milkman"
        if person==3:
            pstr="fireman"
        if person==4:
            pstr="police officer"
        if person==5:
            pstr="weather man"
        tex2=" the shady "+str(pstr)
    elif pt2==3:
        person=random.randint(1,5)
        if person==1:
            pstr="children"
        if person==2:
            pstr="elders"
        if person==3:
            pstr="llamas"
        if person==4:
            pstr="infants"
        if person==5:
            pstr="penguins"
        tex2=" passionate "+str(pstr)
    elif pt2==4:
        tex2=" angry men"
    elif pt2==5:
        tex2=" angry women"
    elif pt2==6:
        tex2=" aliens"
    elif pt2==7:
        person=random.randint(1,3)
        if person==1:
            tex2=" an engineer"
        if person==2:
            tex2=" a doctor"
        if person==3:
            tex2=" an astronaut"
        
    elif pt2==8:
        emo=random.randint(1,3)
        animal=random.randint(1,3)
        if animal==1:
            animals="moose"
        if animal==2:
            animals="duck"
        if animal==3:
            animals="horse"
        if emo==1:
            emot=" an upset "
        elif emo==2:
            emot=" an angry "
        elif emo==3:
            emot=" a frusterated "
        tex2=str(emot)+str(animals)
    elif pt2==9:
        tex2=" a nazi"
    elif pt2==10:
        tex2=" a person"
    if pt3==1:
        tex3=" tenderly"
    elif pt3==2:
        tex3=" gracefully"
    elif pt3==3:
        tex3=" dramatically"
    elif pt3==4:
        tex3=" obnoxiously"
    elif pt3==5:
        tex3=" clearly"
    elif pt3==6:
        tex3=" unkowingly"
    elif pt3==7:
        tex3=" understandably"
    elif pt3==8:
        tex3=" willingly"
    elif pt3==9:
        tex3=" forcefully"
    elif pt3==10:
        tex3=" slowly"
    if pt4==1:
         smack=random.randint(1,5)
         if smack==1:
             smackt="cats."
         elif smack==2:
             smackt="bacon."
         elif smack==3:
             smackt="mathematics."
         elif smack==4:
             smackt="the public broadcasting system."
         elif smack==5:
             smackt="milk."
         tex4=" writes books about "+str(smackt)
    elif pt4==2:
         smack=random.randint(1,5)
         if smack==1:
             smackt="lemons."
         elif smack==2:
             smackt="a beard."
         elif smack==3:
             smackt="cherrys."
         elif smack==4:
             smackt="a communist government."
         elif smack==5:
             smackt="a lampshade."
         tex4=" obtained "+str(smackt)
                    
    elif pt4==3:
         smack=random.randint(1,5)
         if smack==1:
             smackt="sawdust."
         elif smack==2:
             smackt="vanilla extract."
         elif smack==3:
             smackt="fish."
         elif smack==4:
             smackt="hairspray."
         elif smack==5:
             colorc=random.randint(1,3)
             if colorc==1:
                 color="green"
             elif colorc==2:
                 color="red"
             elif colorc==3:
                 color="blue"
             smackt=str(color)+" paint."
         tex4=" began drinking "+str(smackt)
    elif pt4==4:
         smack=random.randint(1,5)
         if smack==1:
             smackt="house."
         elif smack==2:
             smackt="trash can."
         elif smack==3:
             smackt="televison."
         elif smack==4:
             smackt="car."
         elif smack==5:
             smackt="Digital Voice Recorder."
         tex4=" kicked over a "+str(smackt)
    elif pt4==5:
         smack=random.randint(1,5)
         if smack==1:
             smackt="a human."
         elif smack==2:
             smackt="a feature length film."
         elif smack==3:
             smackt="a radio."
         elif smack==4:
             smackt="christmas."
         elif smack==5:
             smackt="the theory of reletivity."
         tex4=" attempted to consume "+str(smackt)
    elif pt4==6:
         smack=random.randint(1,8)
         if smack==1:
             smackt="chicken fingers"
         elif smack==2:
             smackt="transformers"
         elif smack==3:
             smackt="a bannana"
         elif smack==4:
             smackt="Labor Day"
         elif smack==5:
             smackt="a stick"
         elif smack==5:
             smackt="soviet russia"
         elif smack==6:
             smackt="a rubber factory"
         elif smack==7:
             smackt="pocket lint"
         elif smack==8:
             smackt="compressed air"
         tex4=" set "+smackt+" on fire."
    elif pt4==7:
         smack=random.randint(1,10)
         if smack==1:
             smackt="multiple oranges."
         elif smack==2:
             smackt="a clock."
         elif smack==3:
             smackt="an umbrella."
         elif smack==4:
             smackt="Tuesday."
         elif smack==5:
             smackt="agriculture."
         elif smack==6:
             smackt="turkey bacon."
         elif smack==7:
             smackt="mercantilism."
         elif smack==8:
             smackt="economy paper plates."
         elif smack==9:
             smackt="republican sunscreen."
         elif smack==10:
             smackt="democrat sunscreen."
         tex4=" took on the form of "+str(smackt)
    elif pt4==8:
         smack=random.randint(1,5)
         if smack==1:
             smackt="children into piles."
         elif smack==2:
             smackt="democrats into isles."
         elif smack==3:
             smackt="cellphones into stacks."
         elif smack==4:
             smackt="cat food into sections."
         elif smack==5:
             smackt="sticks into groups of "+str(random.randint(1,350))+"."
         tex4=" started to arrange "+str(smackt)
    elif pt4==9:
         smack=random.randint(1,8)
         if smack==1:
             smackt='Your mother was a potato!"'
         elif smack==2:
             smackt='The color orange is a paradox."'
         elif smack==3:
             smackt='Around the world."'
         elif smack==4:
             smackt='The creation of absolute value is a hoax!"'
         elif smack==5:
             smackt='ginger snow is a force not to be tampered with."'
         elif smack==6:
             smackt='why did the chickn cross the road."'
         elif smack==7:
             smackt='science is a lie!"'
         elif smack==8:
             smackt=' argon is the equivalent of mustard."'
         tex4=' yelled aloud "'+str(smackt)
    elif pt4==10:
         smack=random.randint(1,10)
         if smack==1:
             smackt="crush a society."
         elif smack==2:
             smackt="free the south."
         elif smack==3:
             smackt="stock up on teddy bear stuffing."
         elif smack==4:
             smackt="incenerate dog food coupons."
         elif smack==5:
             smackt="wax a car upside down."
         elif smack==6:
             smackt="prepare a turkey."
         elif smack==7:
             smackt="anger a fish."
         elif smack==8:
             smackt="erase the decleration of independence."
         elif smack==9:
             smackt="eat "+str(random.randint(1,30))+"lbs. of liver mush."
         elif smack==10:
             smackt="play hopscotch."
         tex4=" felt the desire to "+str(smackt)
    fulltext=str(tex)+str(tex2)+str(tex3)+str(tex4)
    return fulltext
