#!/usr/bin/env python3

def bayes_factor(sensitivity, specificity):
    """Compute the Bayes factor for a test

    Args:
        sensitivity (float): Sensitivity (true positive rate) as a fraction
        specificity (float): Specificity (true negative rate) as a fraction

    Returns:
        float: The Bayes factor
    """
    false_positive_rate = 1 - specificity
    bayes = sensitivity / (false_positive_rate)
    return bayes

def posterior(sensitivity, specificity, prevalence):
    """Get the posterior probability of the disease given a positive tes

    Args:
        sensitivity (float): Sensitivity (true positive rate) as a fraction
        specificity (float): Specificity (true negative rate) as a fraction
        prevalence (float): Prevelance of the disease as a fraction of the population

    Returns:
        float: Probability of the disease given a positive test as a fraction
    """
    false_positive_rate = 1 - specificity
    p_covid = (prevalence * sensitivity) / (prevalence * sensitivity + false_positive_rate * (1 - prevalence))
    return p_covid

def main():
    desc_str = r"""
                         ____    .-.
                     .-"`    `",( __\_
      .-==:;-._    .'         .-.     `'.
    .'      `"-:'-/          (  \} -=a  .)
   /            \/       \,== `-  __..-'`
'-'              |       |   |  .'\ `;
                  \    _/---'\ (   `"`
                 /.`._ )      \ `;
                 \`-/.'        `"`
                  `"\`-.
                     `"`

A simple little program for calculating Bayesian likelihoods of tests like RATs

This is for 'fun'

!!! Please don't use this as health advice !!!
    """
    print(desc_str)
    try:
        sensitivity = float(input("What is the sensitivity of the test? (as a percentage e.g. 90)\n > "))/100
        specificity = float(input("What is the specificity of the test? (as a percentage e.g. 98)\n > "))/100
        prevalence = float(input("What is the prevalence of the disease? (as a percentage e.g. 1)\n > "))/100
        bayes = bayes_factor(sensitivity, specificity)
        print(f"The Bayes factor is: {bayes:0.1f}" )
        like = posterior(sensitivity, specificity, prevalence)
        print(f"The likelihood of disease with a positive test is: {like*100:0.1f}%")

    except ValueError:
        print("Ivnalid input! Please try again.")
        main()

    print(
    """
Bye!
               _     __,..---""-._                 ';-,
        ,    _/_),-"`             '-.                `\\
       \|.-"`    -_)                 '.                ||
       /`   a   ,                      \              .'/
       '.___,__/                 .-'    \_        _.-'.'
          |\  \      \         /`        _`""""""`_.-'
             _/;--._, >        |   --.__/ `""""""`
           (((-'  __//`'-......-;\      )
                (((-'       __//  '--. /
                          (((-'    __//
                                 (((-'
    """
    )

if __name__ == "__main__":
    main()
