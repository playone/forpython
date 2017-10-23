*** Settings ***
Suite Setup       Go to Homepage
Suite Teardown    Close All Browsers
Library           Selenium2Library

*** Variables ***
${Homepage}       https://www.google.com.tw
${Browser}        Chrome

*** Test Cases ***
test2-1
    Google and search result    spiderman    Homecoming

test2-2
    :FOR    ${list}    IN    ja    fr    de
    \    open browser to page with locale    chrome    http://www.youtube.com    ${list}

test2-3
    [Documentation]    test for loop
    :FOR    ${index}    IN RANGE    2    11    3
    \    log    ${index}

*** Keywords ***
Go to Homepage
    open browser    ${Homepage}    ${Browser}

Google and search result
    [Arguments]    ${searchkey}    ${result}
    Input text    lst-ib    ${searchkey}
    Press Key    lst-ib    \\13
    Wait Until Page Contains    ${result}

Open Firefox to page with the language user want
    [Arguments]    ${locale}    ${url}
    ${profile}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxProfile()    sys
    Call Method    ${profile}    set_preference    intl.accept_languages    ${locale}
    Create WebDriver    Firefox    firefox_profile=${profile}
    Go To    ${url}

Open Chrome to page with the language user want
    [Arguments]    ${locale}    ${url}
    ${option}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${option}    add_argument    --lang\=${locale}
    Create WebDriver    Chrome    chrome_options=${option}
    Go To    ${url}

Open IE to page with the language user want
    ${profile}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxProfile()    sys
    Call Method    ${profile}    set_preference    intl.accept_languages    ${locale}
    Create WebDriver    IE    ie_profile=${profile}
    Go To    ${url}

open browser to page with locale
    [Arguments]    ${browsers}    ${url}    ${locale}
    Run Keyword If    '${browsers}'== 'chrome'    Open Chrome to page with the language user want    ${locale}    ${url}
    ...    ELSE IF    '${browsers}'== 'firefox'    Open Firefox to page with the language user want    ${locale}    ${url}
    ...    ELSE IF    '${browsers}'== 'ie'    Open IE to page with the language user want    ${locale}    ${url}
    Set Selenium Speed    10
