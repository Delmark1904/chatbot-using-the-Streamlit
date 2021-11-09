import streamlit as st

@st.cache(suppress_st_warning=True)
def libs_import():
    from transformers import pipeline
    sentiment_analysis = pipeline("sentiment-analysis")
    return sentiment_analysis


def alaysis(sentence, sentiment_analysis=libs_import()):
    result = sentiment_analysis(sentence)[0]
    print("Label:", result['label'])
    print("Confidence Score:", result['score'])
    if result['label'] == 'POSITIVE':
        return 1
    else:
        return 0


def get_text(key):
    return st.text_input("You: ", "", key = key)


def print_text(t):
    st.write('Bot: ' + t)


def load_data():
    st.title("Test of bot performance")
    st.write("First of all - lets create our campaign")
    # Barbershop
    a = st.text_input('Name of campaign (change it as you want)', value="")
    st.write('Your campaigns name is "' + a + '"')
    goodbye_text = "Ok, sorry for taking your time, have a god day!"
    goodbye_text_call_centre = 'Whould you like me to contact you with call-centre?'
    contact = 'Ok, our worker will contact with you later, have a good day!'
    count_yes = 0
    count_no = 0
    baloons = 0
    call_later = "doesn't want"
    stop = ''
    no_questions = []
    # Hello, my name is Adam, i would like to talk about barbershop industry, if you want to stop dialog - just say "stop".
    hello_text = st.text_input('Add welcome text, that bot will say to lead, also inform lead, that he can stop dialog just saying "stop"', value="")
    if hello_text:
        num = st.selectbox("Now you need to add some questions for you bot. How many questions you want to add?", [i for i in range(10)], index=0)
        name_dict = {}
        for i in range(num):
            name_dict['Question number ' + str(i + 1) + ":"] = ''

            # Do you need to buy something for your hair? yes
            # Would you like to buy a hair clipper? no
            # Would you like to buy one of the offered clipers: blue, red, yellow?
            # Would you like to know more about our products?
        for k, v in name_dict.items():
            name_dict[k] = st.text_input(k, v)

        st.write("Your questions are:")
        for i in range(num):
            st.write(" - " + name_dict['Question number ' + str(i + 1) + ":"])

        b = st.checkbox('Confirm', help='Start dialog with bot')

        if b:
            st.write("Starding dialog...")
            print_text(hello_text)
            ans = get_text(0)
            if ans:
                res = alaysis(ans)
                st.write(res)
                if res:
                    count_yes += 1
                    for i in range(num):
                        print_text(name_dict['Question number ' + str(i + 1) + ":"])
                        ans_main = get_text(i + 1)
                        if ans_main:
                            res_main = alaysis(ans_main)
                            st.write(res_main)
                            if i == num-1 and res_main==1:
                                count_yes += 1
                                print_text(goodbye_text)
                                stop = 'stop'
                                baloons = 1
                            elif i == num-1 and res_main==0:
                                count_no += 1
                                print_text(goodbye_text)
                                stop = 'stop'
                                baloons = 1
                            elif res_main:
                                count_yes += 1
                                continue
                            elif res_main==0 and ans_main!='stop':
                                count_no += 1
                                no_questions.append(i+1)
                                continue
                            else:
                                count_no += 1
                                print_text(goodbye_text_call_centre)
                                ans_main = get_text(i + 2)
                                no_questions.append(i+1)
                                if ans_main:
                                    res_main = alaysis(ans_main)
                                    st.write(res_main)
                                    if res_main:
                                        count_yes += 1
                                        call_later = 'want'
                                        print_text(contact)
                                        stop = 'stop'
                                        baloons = 1
                                    else:
                                        count_no += 1
                                        no_questions.append(i+1)
                                        print_text(goodbye_text)
                                        stop = 'stop'
                                        baloons = 1
                                stop = 'stop'
                                baloons = 1
                                break
                        else:
                            break

                else:
                    count_no += 1
                    no_questions.append(i+1)
                    print_text(goodbye_text)
                    stop = 'stop'
                    baloons = 1

    if stop=='stop':
        st.write('user answerd yes ' + str(count_yes) + ' times')
        st.write('user answerd no ' + str(count_no) + ' times')
        st.write('user answerd no questions:' + str(no_questions))
        st.write('user ' + call_later + ' to call later')

    if baloons:
        st.title('Test done :)')
        st.balloons()



if __name__ == "__main__":
    load_data()



