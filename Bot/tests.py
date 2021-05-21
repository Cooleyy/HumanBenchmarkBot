from webbot import Browser
import time

def get_tests():
    tests = [sequence_memory,  chimp_test, aim_trainer, typing, verbal_memory, number_memory, visual_memory, reaction_time]
    return tests

def sequence_memory(driver: Browser):
    driver.implicitly_wait(0.01)

    squares = driver.find_elements(tag='div', css_selector='div.square')

    roundNo = 1
    squaresNotFound = True
    squareOrder = []
    failSquare = squares[0]
    while roundNo <= 38:
        while squaresNotFound:
            for square in squares:
                if square.get_attribute('class') == 'square active':
                    if len(squareOrder) > 0:
                        if square == squareOrder[-1]:
                            break
                    squareOrder.append(square)
                    if len(squareOrder) == roundNo:
                        squaresNotFound = False
                elif roundNo == 1:
                    failSquare = square

            time.sleep(0.05)

        time.sleep(0.5)
        for square in squareOrder:
            square.click()
            time.sleep(0.001)

        roundNo += 1
        squareOrder = []
        squaresNotFound = True
    time.sleep(1 * roundNo)
    failSquare.click()

def chimp_test(driver: Browser):
    driver.implicitly_wait(0.00001)

    roundNo = 4
    squareOrder = []
    while roundNo <= 40:
        for i in range(1, roundNo+1):
            squareOrder.append(driver.find_elements(text=str(i), tag='div', number=1))

        for i, square in enumerate(squareOrder):
            square[0].find_element_by_xpath('./..').click()

        roundNo += 1
        squareOrder = []
        driver.click('Continue')

def aim_trainer(driver: Browser):
    driver.implicitly_wait(0)

    for i in range(31):
        driver.click(css_selector='div.css-17nnhwz.e6yfngs4', number=1)

def typing(driver: Browser):
    driver.implicitly_wait(0)

    symbols = driver.find_elements(tag='span', classname='incomplete', loose_match=False)
    input = driver.find_elements(css_selector='div.letters.notranslate')[0]

    passage = ""
    for s in symbols:
        passage += s.get_attribute('innerHTML')

    input.send_keys(passage)

def verbal_memory(driver: Browser):
    driver.implicitly_wait(0)
    
    wordElementParent = driver.find_elements(tag='div', css_selector='div.css-1qvtbrk.e19owgy78', loose_match=False)[1]
    round = 1
    words = []
    while round <= 1000:
        word = wordElementParent.get_attribute('innerHTML')[19:-6]
        if word in words:
            driver.click(text='SEEN')
        else:
            words.append(word)
            driver.click(text='NEW')
        round += 1

    for i in range(3):
        word = wordElementParent.get_attribute('innerHTML')[19:-6]
        if word in words:
            driver.click(text='NEW')
        else:
            driver.click(text='SEEN')


def number_memory(driver: Browser):
    round = 1
    while round <= 23:
        num = driver.find_elements(css_selector='div.big-number')[0].get_attribute('innerHTML')
        time.sleep((1*round) + 0.7)
        driver.type(num)
        driver.click('Submit')
        driver.click('NEXT')
        round += 1
    time.sleep((1*round) + 0.7)
    driver.type(str(int(num)-1))
    driver.click('Submit')

def visual_memory(driver: Browser):
    round = 3
    time.sleep(.75)
    container = driver.find_elements(css_selector='div.css-hvbk5q.eut2yre0')[0]
    while round <= 52:
        squares = container.find_elements_by_xpath('.//*//*')
        activeSquares = []
        for square in squares:
            if 'active' in square.get_attribute('class'):
                activeSquares.append(square)
        time.sleep(1)
        for square in activeSquares:
            square.click()
        round +=1
        time.sleep(1.8)

    #Fail out on purpose
    for i in range(3):
        squares = container.find_elements_by_xpath('.//*//*')
        activeSquares = []
        for square in squares:
            if 'active' not in square.get_attribute('class'):
                activeSquares.append(square)
        time.sleep(1)
        for square in activeSquares[:3]:
            square.click()
        time.sleep(1.8)
    

def reaction_time(driver: Browser):
    clickArea = driver.find_elements(tag='div', css_selector='div.e18o0sx0.css-saet2v.e19owgy77')[0]

    round = 1
    while round <= 5:
        if 'view-go' in clickArea.get_attribute('class'):
            clickArea.click()
            round += 1
            clickArea.click()
            time.sleep(0.2)