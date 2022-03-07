from ast import keyword
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

data = [

    {
        "id": "1",
        "volumeInfo": {
            "title": "The Complete Q&A Job Interview Book",
            "authors": [
                "Jeffrey G. Allen"
            ],
            "publisher": "John Wiley & Sons",
            "publishedDate": "2004-04-26",
            "description": "\"The ultimate job interview book! A systematic, foolproof way to generate offers. No job seeker should be without it.\"<br> -National Job Market<br> \"The programmed system works because it is a simple, practical, proven way to interview properly. Use it to win the interview and win the job!\"<br> -Mary Lyon, Associated Press<br> \"Allen's 'Q&A' interview approach eliminates the fear of the unknown, replaces it with the confidence of knowing what to expect, and trains the applicant to get job offers.\"<br> -Kimberly A. Hellyar, Director, Training Consultants International<br> What is a job interview anyway? Is it an objective examination of your experience, skills, and work ethic? Not quite. It's a screen test. You're the actor. In this bestselling guide, Jeff Allen, the world's leading authority on the interview process, shows you how getting hired depends almost completely on the \"actor factor.\" If you know your lines, perfect your delivery, and dress for the part, you'll get hired. If you don't, you won't.<br> In The Complete Q&A Job Interview Book, Jeff develops your own personalized interview script to prepare you in advance for any question that comes your way. Covering questions on everything from personal background to management ability and technological know-how, he gives you a fail-safe delivery format for responding the right way every time. This new edition has been updated to guide you through today's changing job market, and includes an entirely new chapter on dealing with the latest open-ended interrogation questions. If getting a job is playing a part, this is your starring role. Follow the director, and you'll be a superstar!",
            "industryIdentifiers": [
                {
                    "type": "ISBN_10",
                    "identifier": "0471654663"
                },
                {
                    "type": "ISBN_13",
                    "identifier": "9780471654667"
                }
            ],
            "pageCount": 256,
            "categories": [
                "Business & Economics / Careers / General",
                "Business & Economics / General"
            ],
            "imageLinks": {
                "thumbnail": "http://books.google.com/books/content?id=L84QAlsku7MC&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE73l3aLM9p_KDajPAZuc0ahPPY7wYLU3TZ7xzneLRlusha1OyWEdu1rg8C6Eglp3wbr4X_xRa5WvrCcPOu0Y5jxbdR92QhTs91N9mc-VhRX_lvvr90QERlmyk78-neeX3Kkl2tMQ&source=gbs_api"
                }
        }
    },


    {
        "id": "2",
        "volumeInfo": {
            "title": "The Last Interview",
            "subtitle": "A Novel",
            "authors": [
                "Eshkol Nevo"
            ],
            "publisher": "Other Press, LLC",
            "publishedDate": "2020-10-13",
            "description": "<b><b>National Jewish Book Award Finalist<br>Wingate Literary Prize Shortlist <br><b><b>Named a Notable Translated Book of the Year by <i>World Literature Today</i></b> </b> </b><br><br>From the internationally best-selling author of <i>Three Floors Up</i>, a literary page-turner that delves into the deepening cracks in a carefully constructed public persona. </b><br> <br> A writer tries to answer a set of interview questions sent to him by a website editor. At first, they stick to the standard fare: Did you always know you would be a writer? How autobiographical are your books? Have you written any stories you would never publish? Usually his answers in these situations are measured, calculated, cautious. But this time, when his heart is about to break and his life is about to crumble, he finds he cannot tell anything but the truth. The naked, funny, sad, scandalous, politically incorrect truth.<br><br>Every question the writer tackles opens a door to a hidden room of his life. And each of his answers reveals that at the heart of every truth, there is a lie—and vice versa. Surprising, bold, intimate, and utterly engrossing, <i>The Last Interview </i>shows just how tenuous the lines are between work and life, love and hate, fact and fiction. And in exploring the many, often contradictory facets of an Israeli author’s identity, Eshkol Nevo also gives us a nuanced, thought-provoking portrait of a country at odds with itself.",
            "industryIdentifiers": [
                {
                    "type": "ISBN_10",
                    "identifier": "1635429870"
                },
                {
                    "type": "ISBN_13",
                    "identifier": "9781635429879"
                }
            ],
            "pageCount": 480,
            "categories": [
                "Fiction / Psychological",
                "Fiction / Family Life / Marriage & Divorce",
                "Fiction / Jewish"
            ],
            "imageLinks": {
                "thumbnail": "http://books.google.com/books/publisher/content?id=cFL9DwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE71aWBXt9877DkFnkFt9boAZMe3qW2S0_BYiXQvGZjMYoIrJfuUHpnMErZ3YH-B2wkIbZ131otst_MMI6APpDj2O9iRzN54LaeMPR3tsfEp9Gnmhjvd4-3t_ZoIgljzMvzl8r84H&source=gbs_api"
            }
        }
    },


    {
        "id": "3",
        "volumeInfo": {
            "title": "Knock 'em Dead Job Interview",
            "subtitle": "How to Turn Job Interviews Into Job Offers",
            "authors": [
                "Martin Yate"
            ],
            "publisher": "Adams Media",
            "publishedDate": "2012-12-18",
            "description": "<b>Land the job you want!</b><br><br>The interview is one of the most crucial moments of the job search experience and your chance to show your potential employer that you have what it takes to succeed in the position. In order to do that in today's highly competitive job search environment, though, you'll have to find a way to stand out from the crowd.<br><br>Using his twenty-five years of experience, <i>New York Times</i> bestselling author <b>Martin Yate</b> has established a set of rules for job interviews that is sure to get you noticed. Instead of memorizing canned answers, Yate provides you with an explanation of the thought behind more than 300 questions and answers, so that you'll always know what the interviewer is really asking and how you should respond. Packed with information on handling stress questions and weird interview venues, this book also teaches you how to keep your cool--and confidence--from the moment you step inside the building.<br><br>With <i>Knock 'em Dead Job Interview</i>, you will finally be able to differentiate yourself from the competition and score the job!",
            "industryIdentifiers": [
                {
                    "type": "ISBN_10",
                    "identifier": "1440536791"
                },
                {
                    "type": "ISBN_13",
                    "identifier": "9781440536793"
                }
            ],
            "pageCount": 256,
            "categories": [
                "Business & Economics / Careers / General",
                "Business & Economics / Careers / Job Hunting",
                "Business & Economics / General",
                "Self-Help / Personal Growth / Success"
            ],
            "imageLinks": {
                "thumbnail": "http://books.google.com/books/content?id=bCk1uQEACAAJ&printsec=frontcover&img=1&zoom=1&imgtk=AFLRE70ydPnc93V_6Rhji48NVZ2om7748Z6rBDi0lIUlx46EUOQh9W_JOUv8zY8lsI8BrCsaHYviwGcE7ebvX_UU-vLMLiYBppdj4QsSk4Hl4zcie24yDs9QLv27gXRyqxqtEHzT4rcz&source=gbs_api"
            }
        }
    },


    {
        "id": "4",
        "volumeInfo": {
            "title": "The Everything Job Interview Book",
            "subtitle": "All you need to stand out in today's competitive job market",
            "authors": [
                "Lin Grensing-Pophal"
            ],
            "publisher": "Simon and Schuster",
            "publishedDate": "2011-11-18",
            "description": "A job interview can be both terrifying and exciting; interviewees are always eager to put their best foot forward and make a great impression. However, many aspects of this fairly typical business procedure have changed in recent times, and job-hopefuls need to change, too! <i>The Everything Job Interview Book, 3rd Edition</i> is the ultimate manual for today's job-hunter, no matter what their work experience includes, with professional advice on:<ul><li>job hunting and networking;</li><li>how to successfully use social media like Facebook, Twitter, and LinkedIn;</li><li>pre-interview prep work and practice questions;</li><li>what to wear, how to prepare, and when to arrive;</li><li>answering difficult questions honestly and professionally;</li><li>and post-interview follow-up procedures and etiquette.</li></ul> With new and updated sections on social media, guidance for re-entering the workforce, and networking tips, <i>The Everything Job Interview Book, 3rd Edition</i> is the only book job-hunters need to ace the big interview and hear, \"You're hired\".",
            "industryIdentifiers": [
                {
                    "type": "ISBN_10",
                    "identifier": "1440531692"
                },
                {
                    "type": "ISBN_13",
                    "identifier": "9781440531699"
                }
            ],
            "pageCount": 304,
            "categories": [
                "Business & Economics / Careers / General",
                "Business & Economics / Careers / Job Hunting",
                "Business & Economics / General"
            ],
            "imageLinks": {
                "thumbnail": "http://books.google.com/books/publisher/content?id=K-jrDQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE70wXvI7DHWBz9uXNT67pkDFInnRllSvdi0fMUdzmVT3TZkr-VQT9K1L-WrxEaOsz7FAwoStBUkRcMClnaKsR2NZ2OSppyT5ToVuuVAPWONJqzuwYVE1NAZTEJCxQxHfRwAy0-0I&source=gbs_api"
            }
        }
    },


    {
        "id": "5",
        "volumeInfo": {
            "title": "Perfect Phrases for the Perfect Interview: Hundreds of Ready-to-Use Phrases That Succinctly Demonstrate Your Skills, Your Experience and Your Value in Any Interview Situation",
            "subtitle": "Hundreds of Ready-to-Use Phrases That Succinctly Demonstrate Your Skills, Your Experience and Your V",
            "authors": [
                "Carole Martin"
            ],
            "publisher": "McGraw Hill Professional",
            "publishedDate": "2005-04-21",
            "description": "<p><b>Hundreds of interview-acing words and phrases to land you the job</b></p> <p>In a job interview, every word counts. That's why you need to make sure you'll be prepared with exactly the right answers to any question an interviewer might throw at you. With <i>Perfect Phrases for the Perfect Interview</i>, you will be equipped to handle even the toughest questions. This ready reference supplies you with:</p> <ul> <li>The best answers to a wide range of interview questions, from icebreaker questions about experience to questions about specific skills to the dreaded \"Why did you leave (or get fired from) your last job?\"</li> <li>Exercises and resources that help you prepare for the big day</li> <li>Tips on words to avoid and on how you can convince a potential employer that you are perfect for the job</li> </ul>",
            "industryIdentifiers": [
                {
                    "type": "ISBN_10",
                    "identifier": "0071466436"
                },
                {
                    "type": "ISBN_13",
                    "identifier": "9780071466431"
                }
            ],
            "pageCount": 240,
            "categories": [
                "Business & Economics / Careers / General",
                "Self-Help / Personal Growth / Success"
            ],
            "imageLinks": {
                "thumbnail": "http://books.google.com/books/content?id=m4qGDGglsqIC&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE7219e8-9Gq-oykmy3ozUOnKR9yTZN9WPoXBjZseru1p8G_MOgI7EBbmVYhFEDgKIveoX7U0CdzbW6-45QFRTeyBa5aNYkEODuueODI2m6FrZmcpD4d8gIQ6RDFeE45fpocTSn8c&source=gbs_api"
            }
        }
    },


    {
        "id": "6",
        "volumeInfo": {
            "title": "The Interview Book",
            "subtitle": "Your definitive guide to the perfect interview",
            "authors": [
                "James Innes"
            ],
            "publisher": "Pearson UK",
            "publishedDate": "2012-12-14",
            "description": "<p>The UK’s bestselling guide to successful interviews is back, with a new editionupdated with expanded content on planning for interviews and tailoring your interview to a specific role.</p><p><i> </i></p><p>This is the definitive, bestselling guide to planning, preparing and performing in interviews to maximise your chances of landing the job you want. The guidance in this book has been tried, tested and honed to perfection. The unique content includes a chapter on avoiding the most common interview mistakes, and important information on how to handle and benefit from the post-interview period.</p><p> </p><p>Written by the CEO of the UK’s leading CV consultancy service, James Innes, the book is supported by exclusive online tools and bonus content including sample interview questions, templates and best-practice scenarios.</p>",
            "industryIdentifiers": [
                {
                    "type": "ISBN_13",
                    "identifier": "9780273776659"
                },
                {
                    "type": "ISBN_10",
                    "identifier": "0273776657"
                }
            ],
            "pageCount": 312,
            "categories": [
                "Education / Counseling / Career Development",
                "Self-Help / Personal Growth / Success"
            ],
            "imageLinks": {
                "thumbnail": "http://books.google.com/books/content?id=2rfPGkgaeTAC&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE72vAK6Ju9naPJlFLrBV2hHUrfLjWSOagA3tRW7SBWVcG4DZPCPyMepACpxQY-H3KlJEACzQFEUbSBOVkkcpsnRoW4u1ArZEwCZfq4tptkf7Lh5tHSfzUVT1FKkCPFvCJcjS96KU&source=gbs_api",
            }
        }
    },


    {
        "id": "7",
        "volumeInfo": {
            "title": "The Most Important Questions to Ask on Your Next Job Interview",
            "subtitle": "Insider Secrets You Need to Know",
            "authors": [
                "Kendall Blair"
            ],
            "publisher": "Atlantic Publishing Company",
            "publishedDate": "2007",
            "description": "<p>You have brushed up on the tough interview questions. You have covered every area of your resume including that three month unemployment gap and you have studied up on the company. But there is one more thing you may not have thought of some questions you want to ask in your interview. Many prospective employees do not realize, or forget, that the interview process is a two way street. When the formal interview is over and the interviewer asks if you have any questions, now is the time to distance yourself from the competition. <p>You should be asking questions to determine whether you would be happy in the position or with the company, but you need to ask the right questions. The questions you ask will help show what you can contribute to the organization. They also can help you figure out if you want this job. In this groundbreaking new book you will find over two hundred of the RIGHT kinds of questions to ask. You will be able to stand out from the others competing for the job and gain valuable insight into what working for a company would be like. <p>Atlantic Publishing is a small, independent publishing company based in Ocala, Florida. Founded over twenty years ago in the company president's garage, Atlantic Publishing has grown to become a renowned resource for non-fiction books. Today, over 450 titles are in print covering subjects such as small business, healthy living, management, finance, careers, and real estate. Atlantic Publishing prides itself on producing award winning, high-quality manuals that give readers up-to-date, pertinent information, real-world examples, and case studies with expert advice. Every book has resources, contact information, and web sites of the products or companies discussed. <p></p>",
            "industryIdentifiers": [
                {
                    "type": "ISBN_10",
                    "identifier": "1601381336"
                },
                {
                    "type": "ISBN_13",
                    "identifier": "9781601381330"
                }
            ],
            "pageCount": 144,
            "categories": [
                "Business & Economics / Careers / Job Hunting"
            ],
            "imageLinks": {
                "thumbnail": "http://books.google.com/books/content?id=JR7AQ6IZtlIC&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE71KuNh4hTgASTDdDtJmU-bCk5yUNs3rOA7tSV9JtAzGKqnDiGqaCUTvqApZ89EEo_6Qf59AmIe_h4lMbdp-aaMUxdjJUQvr_78c3drHM1J6zBgyvxEGQrMbENCF_qhP3kEMObi1&source=gbs_api",
            }
        }
    },


    {
        "id": "8",
        "volumeInfo": {
            "title": "Stellar Interview Performance",
            "subtitle": "Guide to Ace Interviews",
            "authors": [
                "Vinod Joshi"
            ],
            "publisher": "Notion Press",
            "publishedDate": "2019-04-10",
            "description": "<p>Do you ever wish you knew what interviewers look for during interviews? Ever wondered why some people seem to breeze through interviews while others struggle? Are you overwhelmed by the amount of preparation needed for different types of interviews? Do you want to feel confident and ready before every interview?<br> <br> Look no further, as this book, “Stellar Interview Performance” written by an experienced corporate consultant and a seasoned interviewer, is your one-stop shop to delivering your best interview performance!<br> <br> For every professional, interviews are an essential stepping-stone to getting the next big career break. Whether you are a new graduate straight out of college or a seasoned executive, the progress of your career depends on your ability to display your best self during interviews.<br> <br> What’s inside this book?<br> <br> • Insights into the interview process from the interviewer’s point of view<br> • Step-by-step instructions from applying for a job to appearing for the final interview<br> • Practical guidance to hone your communication skills<br> • Easy-to fill-out checklists to help you get organized before interviews<br> • Dozens of sample interview questions for practice.</p>",
            "industryIdentifiers": [
                {
                    "type": "ISBN_10",
                    "identifier": "1643246658"
                },
                {
                    "type": "ISBN_13",
                    "identifier": "9781643246659"
                }
            ],
            "pageCount": 90,
            "categories": [
                "Business & Economics / Careers / Job Hunting"
            ],
            "imageLinks": {
                "thumbnail": "http://books.google.com/books/publisher/content?id=aZaRDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE71Yv-LM5x64gmUtk5KlLL-o7FJYGV47BLeOavZGv05mOFUNaudEjvxZMtVdit97jlonkRmWDM1cP1utLgGWr_gzcEpHkwD8x19DmRwuVwFmM3Mn9vWP4Lo65zZz9JlZ5BdZlE50&source=gbs_api",
            }
        }
    },


    {
        "id": "9",
        "volumeInfo": {
            "title": "The Interview Question & Answer Book",
            "subtitle": "Your definitive guide to the best answers to even the toughest interview question",
            "authors": [
                "James Innes"
            ],
            "publisher": "Pearson UK",
            "publishedDate": "2013-07-09",
            "description": "<p>Take the fear out of your interview and never be stuck for the right answer to even the toughest questions with <i>The Interview Question and Answer Book</i>.</p><p>The job market is fierce, competition has never been greater and it’s vital that you can grab every opportunity for competitive advantage and stay one step ahead. Interviewers are looking for people who really stand out, and here's your chance to be different from the rest.</p><p>Written by one of the UK’s leading careers experts and bestselling author of <i>The Interview Book</i>, this definitive guide to questions and answers encourages every job-hunter to think on your feet and express your individuality whilst supplying ideal responses to interview questions so that you’re seen as the ideal candidate for the job.</p>",
            "industryIdentifiers": [
                {
                    "type": "ISBN_10",
                    "identifier": "0273781561"
                },
                {
                    "type": "ISBN_13",
                    "identifier": "9780273781561"
                }
            ],
            "pageCount": 232,
            "categories": [
                "Self-Help / Personal Growth / Success"
            ],
            "imageLinks": {
                "thumbnail": "http://books.google.com/books/publisher/content?id=CaQDAAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE72F8jrZ5qL5RklOsNGyVTTtdzaZzZC9SoyAgjkgS7POLkK_hed7rPBvatZ429s8ZfoMI-dH25Y3i5jdRsSVj2CIrMIGJD9SMYg1voPqRKE0KDc0VO9BY96wqFreXx0VZRH5jqM3&source=gbs_api",
            }
        }
    },


    {
        "id": "10",
        "volumeInfo": {
            "title": "The Long Interview",
            "authors": [
                "Grant McCracken"
            ],
            "publisher": "SAGE",
            "publishedDate": "1988-09",
            "description": "<p><b>The Long Interview </b>provides a systematic guide to the theory and methods of the long qualitative interview or intensive interviewing. It gives a clear explanation of one of the most powerful tools of the qualitative researcher. The volume begins with a general overview of the character and purpose of qualitative inquiry and a review of key issues. The author outlines the four steps of the long qualitative interview and how to judge quality. He then offers practical advice for those who commission and administer this research, including sample questionnaires and budgets to help readers design their own. The author introduces key theoretical and methodological issues, various research strategies, and a simple four-stage model of inquiry, from the design of an open-ended questionnaire to the write up of results. </p>",
            "industryIdentifiers": [
                {
                    "type": "ISBN_10",
                    "identifier": "0803933533"
                },
                {
                    "type": "ISBN_13",
                    "identifier": "9780803933538"
                }
            ],
            "pageCount": 88,
            "categories": [
                "Business & Economics / Careers / General",
                "Language Arts & Disciplines / General",
                "Social Science / Research"
            ],
            "imageLinks": {
                "thumbnail": "http://books.google.com/books/content?id=3N01cl2gtoMC&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE70e0eJNw_ZZsKU-Rz4t2nuJIF9jPFW_8-NUw4ldv-qhfjgiHVjZGi7DKkP7-ErBLUK7fSqkx1KFVU-J3zSPAwuSwtsTETelh9BJG9B_h-kkmfPNK1g-7TU95Zk0F45OKqh4Dk7T&source=gbs_api",
            }
        }
    }

    
]


# ROUTES

@app.route('/')
def default():
   return render_template('home.html')   

@app.route('/home')
def home():
   return render_template('home.html')  

@app.route('/view/<id>', methods=['GET', 'POST'])
def get_details(id = None):

    global data

    print("/get_details")
    print(id)
    print(type(id))

    index = None
    for i in range(len(data)):
        if data[i]["id"] == id:
            index = i

    return render_template('view.html', item = data[index])


@app.route('/search_results/<keyword>', methods=['GET', 'POST'])
def search_results(keyword = None):

    global data

    print("search_results")

    # json_data = request.get_json()   
    # kw = json_data["keyword"] 
    print(keyword)
    print(type(keyword))

    search_list = {}
    for i in range(len(data)):
        if keyword in data[i]["volumeInfo"]["title"]:
            print(data[i]["volumeInfo"]["title"])
            search_list[data[i]["id"]]  = data[i]["volumeInfo"]["title"]

    print(search_list)
    return render_template('search.html', search_list = search_list, keyword = keyword)



@app.route('/get_item', methods=['GET', 'POST'])
def get_item():

    global data 

    json_data = request.get_json()   
    id = json_data["id"] 
    print(id)
    print(type(id))

    item = data[int(id) - 1]

    return jsonify(item = item)



if __name__ == '__main__':
   app.run(debug = True)
