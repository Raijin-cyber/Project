print("Hello There" + "\nI am Dixcot, your personal dietition.")
print("What should I call you?")
name=input("\t")
print("Okay, from now on I'll call you by your name",name,"\nTell me how are you feeling in given below options? \ngood\naverage\nbad")
status=input("\t")
if (status == "good"):
    print("Keep it up. Do you need tips to keep going?")
    a3=input("\ty or n\n")
    if(a3 == "y"):
        print(''' Here are some tips which you can follow to help that good feeling😀
                    Set Realistic Goals: Start with small, achievable changes to avoid feeling overwhelmed.
                    Meal Prep: Prepare meals in advance to reduce the temptation of unhealthy options.
                    Keep a Food Journal: Track what you eat to stay mindful of your choices.
                    Healthy Snacks: Keep nutritious snacks handy to curb cravings without straying from your diet.
                    Find Support: Share your goals with friends or join a community for motivation and accountability.''')
        z=input("Wanna close? Press enter")
    elif(a3 == "n"):
        print("See ya later🙋‍")
        y=input("wanna close? press enter")
elif(status == "average"):
    print("Do you need help to get you at your fullest potential?")
    ans=input("y OR n\n")
    if (ans == "y"):
        print("This is what I was thinking about,\ngood choice",name,"\nNow tell me what you ate recently?")
        a1=input("junk or healthy\n")
        if(a1=="junk"):
            print("Trust me you really need a plan")
            print("You need to follow this for 7 days, remember change will be gradual not sudden.")
            print('''
                Sunbday
                Breakfast (8:00-8:30AM)    Aloo Paratha (2) + Raita (1 cup)
                Mid-Meal (11:00-11:30AM)    Fruit Salad (1 cup) + Tender Coconut Water (1 glass)
                Lunch (2:00-2:30PM)    1 cup moong dal + 1 cup bhindi + 2 chapatti + salad
                Evening (4:00-4:30PM)    Tea/ Coffee (1 cup) + Boiled Chana Chat (1 cup)
                Dinner (8:00-8:30PM)    Chapati (2) + Jeera Aloo (1 cup)
                Monday
                Breakfast (8:00-8:30AM)    Chapati (2) + Daal (1 cup)
                Mid-Meal (11:00-11:30AM)    Fruit Salad (1 cup) + Tender Coconut Water (1 glass)
                Lunch (2:00-2:30PM)    1 cup rajma + 1 cup gobhi aloo + 1 cup cucumber raita + 1 cup rice + 1 chapatti
                Evening (4:00-4:30PM)    Tea/ Coffee (1 cup) + Aloo Chat (1 cup)
                Dinner (8:00-8:30PM)    Chapati (2) + Mix Veg.
                Tuesday
                Breakfast (8:00-8:30AM)    Cheela (2) + Raita (1 cup)
                Mid-Meal (11:00-11:30AM)    Fruit Salad (1 cup) + Tender Coconut Water (1 glass)
                Lunch (2:00-2:30PM)    1 cup chicken curry + 1 cup boiled rice + 2 chapatti + salad
                Evening (4:00-4:30PM)    Tea/ Coffee (1 cup) + Papri Chat (1 cup)
                Dinner (8:00-8:30PM)    Chapati (2) + Fish Curry (1 cup)
                Wednesday
                Breakfast (8:00-8:30AM)    Veg. Poha (1 cup) + Raita (1/2 cup)
                Mid-Meal (11:00-11:30AM)    Fruit Salad (1 cup) + Tender Coconut Water (1 glass)
                Lunch (2:00-2:30PM)    1 cup white chana + palak paneer + 1 cup rice + 1 chapatti + salad
                Evening (4:00-4:30PM)    Tea/ Coffee (1 cup) + Mur-mure Chat (1 cup)
                Dinner (8:00-8:30PM)    Chapati (2) + Mustard Greens (1 cup)
                Thursday
                Breakfast (8:00-8:30AM)    Aloo Paratha (2) + Raita (1 cup)
                Mid-Meal (11:00-11:30AM)    Fruit Salad (1 cup) + Tender Coconut Water (1 glass)
                Lunch (2:00-2:30PM)    1 cup soy bean curry + 1 cup tinda vegetable + 2 chapatti + salad
                Evening (4:00-4:30PM)    Tea/ Coffee (1 cup) + Boiled Chana Chat (1 cup)
                Dinner (8:00-8:30PM)    Chapati (2) + Bottle Gourd Curry (1 cup)
                Friday
                Breakfast (8:00-8:30AM)    Chapati (2) + Daal (1 cup)
                Mid-Meal (11:00-11:30AM)    Fruit Salad (1 cup) + Tender Coconut Water (1 glass)
                Lunch (2:00-2:30PM)    1 cup fish curry + 1 cup boiled rice + 1 chapatti + 1 cup ghia raita + salad
                Evening (4:00-4:30PM)    Tea/ Coffee (1 cup) + Aloo Chat (1 cup)
                Dinner (8:00-8:30PM)    Chapati (2) + Matar n Mushroom Curry (1 cup)
                Saturday
                Breakfast (8:00-8:30AM)    Veg Upma (1 cup) + Raita (1/2 cup)
                Mid-Meal (11:00-11:30AM)    Fruit Salad (1 cup) + Tender Coconut Water (1 glass)
                Lunch (2:00-2:30PM)    1 cup chicken curry + 1 cup rice + salad
                Evening (4:00-4:30PM)    Tea/ Coffee (1 cup) + Papri Chat (1 cup)
                Dinner (8:00-8:30PM)    Chapati (2) + Kofta (1 cup)''')
            m=input("Wanna exit?,press enter")
        elif(a1=="healthy"):
            print("Looks like you need some changes in your habits",name,"Okay I have gotta suggest some changes to your plan.")
            print('''
                1-Diverse Diet: Include a wide variety of fruits, vegetables, and whole grains.
                2-Probiotics: Add yogurt or fermented foods for gut health.
                3-Omega-3s: Incorporate sources like fish, flaxseeds, and walnuts.
                4-Hydration: Drink plenty of water, herbal teas, and limit sugary drinks.
                5-Protein Balance: Mix plant-based proteins (beans, lentils) with lean meats.
                6-Healthy Fats: Use olive oil, avocado, and nuts instead of trans fats.
                7-Limit Processed Foods: Cut down on fast food, chips, and sugary snacks.
                8-Portion Control: Eat smaller, more frequent meals to avoid overeating.
                9-Fiber-Rich Foods: Include oats, brown rice, and legumes to improve digestion.
                10-Mindful Eating: Chew slowly and focus on your meal to avoid overeating.''')
            print("Do you need more suggestions?")
            a2=input("\ty or n\n")
            if(a2=="y"):
                print('''Seasonal Eating: Focus on consuming seasonal and locally sourced produce.
                        Cut Down on Sugar: Reduce added sugars in your diet, including in beverages and snacks.
                        Whole Grains: Switch to whole grain versions of bread, pasta, and cereals.
                        Meal Planning: Plan your meals ahead to ensure balanced nutrition and avoid unhealthy choices.
                        Limit Salt Intake: Reduce your consumption of salty foods and use herbs and spices for flavor instead.''')
                x=input()
            elif(a2=="n"):
                print("Closing")
                u=input()
    elif(ans == "n"):
        print("wanna exit? Press enter")
        v=input()
elif(status == "bad"):
    print("You need special attention towards your health")
    print('''Here are 10 reasons that might be keeping you from acheiving your fullest potential
            Stress or Anxiety: Ongoing stress or anxiety about work, studies, relationships, or other aspects of life.
            Lack of Sleep: Poor sleep quality or insufficient sleep can affect mood and energy levels.
            Poor Diet: Consuming unhealthy food or not getting enough nutrients can lead to feeling physically and mentally unwell.
            Physical Illness: Feeling unwell due to a cold, flu, or other health issues can impact your mood.
            Lack of Exercise: A sedentary lifestyle can contribute to low energy and a negative mood.
            Social Isolation: Lack of social interaction or support can lead to feelings of loneliness and sadness.
            Unresolved Emotions: Holding onto anger, sadness, or grief can weigh heavily on your mood.
            Negative Thought Patterns: Constant negative thinking or self-criticism can lead to feeling bad.
            Hormonal Imbalances: Hormonal changes, such as those related to thyroid issues, menstruation, or menopause, can affect mood.
            Overwork or Burnout: Working too much without proper rest can lead to physical and emotional exhaustion.''')
    print('''\n\nHere is your diet plan:
                Morning
                    Start with Water: Drink a glass of warm water with lemon to hydrate and boost your metabolism.
                Breakfast:
                    Oats with Fruits: Oatmeal topped with fresh berries, a banana, and a sprinkle of nuts or seeds.
                    Protein Option: A boiled egg or Greek yogurt for protein.
                    Herbal Tea: Green tea or chamomile to start your day calmly.
                    Mid-Morning Snack
                    Fruit: A piece of fruit like an apple, orange, or a handful of berries.
                    Nuts: A small handful of almonds or walnuts for healthy fats and energy.
                Lunch
                    Protein-Rich Salad:
                    Grilled chicken or tofu on a bed of mixed greens (spinach, kale, arugula).
                    Add colorful veggies like bell peppers, tomatoes, and cucumbers.
                    Include a portion of quinoa or brown rice for complex carbs.
                    Dress with olive oil and lemon juice.
                Afternoon Snack
                    Yogurt with Honey: A small bowl of plain yogurt with a drizzle of honey and a sprinkle of chia seeds or flaxseeds.
                    Dark Chocolate: A small piece (70% cocoa or higher) for an antioxidant boost.
                Dinner
                    Lean Protein and Veggies:
                    Grilled or baked salmon, chicken breast, or a plant-based protein like lentils.
                    Steamed or roasted veggies like broccoli, carrots, and sweet potatoes.
                    A side of whole grains like brown rice or quinoa.
                    Hydration: Drink water or herbal tea (peppermint or chamomile) to wind down.
                Evening Snack (Optional)
                    Herbal Tea: A calming tea like chamomile or lavender.
                    Light Snack: A small portion of mixed nuts or a banana for potassium, which helps regulate mood.
            Additional Tips:
                Stay Hydrated: Drink plenty of water throughout the day to keep energy levels up.
                Limit Caffeine: Too much caffeine can increase anxiety and disrupt sleep.
                Reduce Sugar: Avoid sugary snacks and drinks that can lead to mood swings.
                Eat Regularly: Don’t skip meals to maintain stable blood sugar levels and avoid irritability.
                Mindful Eating: Eat slowly and focus on your food to enjoy and fully digest it.

                If feelings of being unwell persist, consider consulting a healthcare provider or nutritionist.
                Hope you'll get well soon 😀''')
    n=input("wanna close? press enter")
else:
    print("Invalid response")
    w=input("exit?")


