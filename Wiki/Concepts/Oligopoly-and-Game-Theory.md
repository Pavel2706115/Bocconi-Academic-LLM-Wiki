---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Microeconomics]]"
status: seed
created: 2026-05-18
updated: 2026-05-21
sources:
  - "Raw/Sources/30065 ECONOMICS - MODULE 1 (MICROECONOMICS)/C17.md"
  - "Raw/Sources/30065 ECONOMICS - MODULE 1 (MICROECONOMICS)/C18.md"
  - "Raw/Sources/30065 ECONOMICS - MODULE 1 (MICROECONOMICS)/C19.md"
  - "Raw/Sources/Economics-for-Dummies.md"
source_count: 4
aliases:
  - "Game Theory"
  - "Nash Equilibrium"
  - "Cournot"
  - "Bertrand"
---

# Oligopoly and Game Theory

## Definition

An oligopoly is a market structure characterized by a small number of large, mutually interdependent firms. Because the actions of one firm directly impact the profits of others, firms cannot make decisions in isolation. **Game Theory** provides the mathematical and analytical framework to model this strategic interaction.

## Game Theory Foundations

A "game" in economics consists of three core components:
1.  **Players**: The decision-makers (in this case, the oligopolistic firms).
2.  **Strategies**: The complete set of actions or choices available to each player (e.g., choosing a high or low price, producing a high or low quantity).
3.  **Payoffs**: The outcomes or rewards (usually economic profits) resulting from each possible combination of strategies selected by all players.

### The Nash Equilibrium
A **Nash Equilibrium** is a situation in which each player chooses their best strategy *given the strategies chosen by the other players*. At a Nash Equilibrium, no player has a unilateral incentive to deviate or change their decision, as doing so would result in a lower or equal payoff.

---

## Oligopoly Models

Oligopolistic firms interact in different ways, leading to distinct market outcomes:

### 1. Cournot Quantity Competition
Firms choose their **production quantities** simultaneously and independently. 
- *Mechanism*: A single market price is established based on the total quantity produced by all firms.
- *Outcome*: Cournot equilibrium output is higher than a monopoly's output but lower than perfect competition's output. The price is lower than monopoly but higher than marginal cost.

### 2. Bertrand Price Competition
Firms choose their **selling prices** simultaneously and independently, selling identical products.
- *Mechanism*: Consumers buy entirely from the firm offering the lowest price. If prices are equal, they split the market.
- *Outcome*: This leads to the **Bertrand Paradox**: firms repeatedly undercut each other's prices until price is driven down to marginal cost ($P = MC$). At this point, firms earn zero economic profit, replicating the perfectly competitive outcome despite there being only two firms (duopoly).
- *Resolving the Paradox*: If products are differentiated (non-identical) or firms face capacity constraints, the Bertrand price does not fall all the way to marginal cost.

### 3. Stackelberg Leader-Follower Model
Firms compete on quantity sequentially. A dominant "leader" firm chooses its quantity first, anticipating how the "follower" firm will react. The leader enjoys a first-mover advantage, capturing a larger market share and higher profits.

---

## Collusion, Cartels, and the Prisoner's Dilemma

Firms in an oligopoly have a strong incentive to cooperate: by coordinating to restrict output and raise prices, they can behave collectively as a monopoly and maximize joint profits (**collusion**). A formal collusive agreement is called a **cartel** (e.g., OPEC).

### Instability of Cartels
Cartels are notoriously unstable because each member faces a strong incentive to cheat on the agreement:
- If all other members restrict output to keep prices high, one member can quietly expand its own output, selling more units at the high price and dramatically increasing its individual profit.
- If *all* members cheat, the market supply increases, the price collapses, and cartel profits evaporate.

### The Prisoner's Dilemma
This strategic conflict is modeled by the **Prisoner's Dilemma**, a game showing why two rational players might fail to cooperate even when doing so is in their joint interest:

```
                  Firm B (Cooperate)     Firm B (Cheat)
Firm A (Cooperate)     ($10M, $10M)           ($2M, $15M)
Firm A (Cheat)         ($15M, $2M)            ($5M, $5M)
```

In this game, "Cheat" is a **dominant strategy** for both firms — it is the best choice regardless of what the competitor does. As a result, both firms cheat, leading to a Nash Equilibrium of (Cheat, Cheat) with payoffs of ($5M, $5M), which is strictly worse than the cooperative outcome of ($10M, $10M).

## Related Concepts

- [[Wiki/Concepts/Perfect-Competition|Perfect Competition]]
- [[Wiki/Concepts/Monopoly|Monopoly]]
- [[Wiki/Concepts/Market-Equilibrium|Market Equilibrium]]
