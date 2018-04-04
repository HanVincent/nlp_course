
# coding: utf-8

# In[1]:


akl = dict( [ (x+'-n', True) for x in 'focus, ability, absence, account, achievement, act, action, activity, addition, adoption, adult, advance, advantage, advice, age, aim, alternative, amount, analogy, analysis, application, approach, argument, aspect, assertion, assessment, assistance, association, assumption, attempt, attention, attitude, author, awareness, balance, basis, behaviour, behavior, being, belief, benefit, bias, birth, capacity, case, category, cause, centre, challenge, change, character, characteristic, choice, circumstance, class, classification, code, colleague, combination, commitment, committee, communication, community, comparison, complexity, compromise, concentration, concept, conception, concern, conclusion, condition, conduct, conflict, consensus, consequence, consideration, constraint, construction, content, contradiction, contrast, contribution, control, convention, correlation, country, creation, crisis, criterion, criticism, culture, damage, data, debate, decision, decline, defence, defense, definition, degree, demand, description, destruction, determination, development, difference, difficulty, dilemma, dimension, disadvantage, discovery, discrimination, discussion, distinction, diversity, division, doctrine, effect, effectiveness, element, emphasis, environment, error, essence, establishment, evaluation, event, evidence, evolution, examination, example, exception, exclusion, existence, expansion, experience, experiment, explanation, exposure, extent, extreme, fact, factor, failure, feature, female, figure, finding, force, form, formation, function, future, gain, group, growth, guidance, guideline, hypothesis, idea, identity, impact, implication, importance, improvement, increase, indication, individual, influence, information, insight, instance, institution, integration, interaction, interest, interpretation, intervention, introduction, investigation, isolation, issue, kind, knowledge, lack, learning, level, likelihood, limit, limitation, link, list, literature, logic, loss, maintenance, majority, male, manipulation, mankind, material, means, measure, medium, member, method, minority, mode, model, motivation, movement, need, network, norm, notion, number, observation, observer, occurrence, operation, opportunity, option, organisation, organization, outcome, output, paper, parallel, parent, part, participant, past, pattern, percentage, perception, period, person, personality, perspective, phenomenon, point, policy, population, position, possibility, potential, practice, presence, pressure, problem, procedure, process, production, programme, program, progress, property, proportion, proposition, protection, provision, publication, purpose, quality, question, range, rate, reader, reality, reason, reasoning, recognition, reduction, reference, relation, relationship, relevance, report, representative, reproduction, requirement, research, resistance, resolution, resource, respect, restriction, result, review, rise, risk, role, rule, sample, scale, scheme, scope, search, section, selection, sense, separation, series, service, set, sex, shift, significance, similarity, situation, skill, society, solution, source, space, spread, standard, statistics, stimulus, strategy, stress, structure, subject, success, summary, support, survey, system, target, task, team, technique, tendency, tension, term, theme, theory, tolerance, topic, tradition, transition, trend, type, uncertainty, understanding, unit, use, validity, value, variation, variety, version, view, viewpoint, volume, whole, work, world'.split(', ') ]+            [ (x+'-v', True)  for x in 'accept, account, achieve, acquire, act, adapt, adopt, advance, advocate, affect, aid, aim, allocate, allow, alter, analyse, analyze, appear, apply, argue, arise, assert, assess, assign, associate, assist, assume, attain, attempt, attend, attribute, avoid, base, be, become, benefit, can, cause, characterise, characterize, choose, cite, claim, clarify, classify, coincide, combine, compare, compete, comprise, concentrate, concern, conclude, conduct, confine, conform, connect, consider, consist, constitute, construct, contain, contrast, contribute, control, convert, correspond, create, damage, deal, decline, define, demonstrate, depend, derive, describe, design, destroy, determine, develop, differ, differentiate, diminish, direct, discuss, display, distinguish, divide, dominate, effect, eliminate, emerge, emphasize, employ, enable, encounter, encourage, enhance, ensure, establish, evaluate, evolve, examine, exceed, exclude, exemplify, exist, expand, experience, explain, expose, express, extend, facilitate, fail, favour, favor, finance, focus, follow, form, formulate, function, gain, generate, govern, highlight, identify, illustrate, imply, impose, improve, include, incorporate, increase, indicate, induce, influence, initiate, integrate, interpret, introduce, investigate, involve, isolate, label, lack, lead, limit, link, locate, maintain, may, measure, neglect, note, obtain, occur, operate, outline, overcome, participate, perceive, perform, permit, pose, possess, precede, predict, present, preserve, prevent, produce, promote, propose, prove, provide, publish, pursue, quote, receive, record, reduce, refer, reflect, regard, regulate, reinforce, reject, relate, rely, remain, remove, render, replace, report, represent, reproduce, require, resolve, respond, restrict, result, retain, reveal, seek, select, separate, should, show, solve, specify, state, stimulate, strengthen, stress, study, submit, suffer, suggest, summarise, summarize, supply, support, sustain, tackle, tend, term, transform, treat, undermine, undertake, use, vary, view, write, yield'.split(', ') ]+            [ (x+'-adj', True) for x in 'absolute, abstract, acceptable, accessible, active, actual, acute, additional, adequate, alternative, apparent, applicable, appropriate, arbitrary, available, average, basic, central, certain, clear, common, competitive, complete, complex, comprehensive, considerable, consistent, conventional, correct, critical, crucial, dependent, detailed, different, difficult, distinct, dominant, early, effective, equal, equivalent, essential, evident, excessive, experimental, explicit, extensive, extreme, far, favourable, favorable, final, fixed, following, formal, frequent, fundamental, future, general, great, high, human, ideal, identical, immediate, important, inadequate, incomplete, independent, indirect, individual, inferior, influential, inherent, initial, interesting, internal, large, late, leading, likely, limited, local, logical, main, major, male, maximum, mental, minimal, minor, misleading, modern, mutual, natural, necessary, negative, new, normal, obvious, original, other, overall, parallel, partial, particular, passive, past, permanent, physical, positive, possible, potential, practical, present, previous, primary, prime, principal, productive, profound, progressive, prominent, psychological, radical, random, rapid, rational, real, realistic, recent, related, relative, relevant, representative, responsible, restricted, scientific, secondary, selective, separate, severe, sexual, significant, similar, simple, single, so-called, social, special, specific, stable, standard, strict, subsequent, substantial, successful, successive, sufficient, suitable, surprising, symbolic, systematic, theoretical, total, traditional, true, typical, unique, unlike, unlikely, unsuccessful, useful, valid, valuable, varied, various, visual, vital, wide, widespread'.split(', ') ]+            [ (x+'-adv', True) for x in 'above, accordingly, accurately, adequately, also, approximately, at best, basically, clearly, closely, commonly, consequently, considerably, conversely, correctly, directly, effectively, e.g., either, equally, especially, essentially, explicitly, extremely, fairly, far, for example, for instance, frequently, fully, further, generally, greatly, hence, highly, however, increasingly, indeed, independently, indirectly, inevitably, initially, in general, in particular, largely, less, mainly, more, moreover, most, namely, necessarily, normally, notably, often, only, originally, over, partially, particularly, potentially, previously, primarily, purely, readily, recently, relatively, secondly, significantly, similarly, simply, socially, solely somewhat, specifically, strongly, subsequently, successfully, thereby, therefore, thus, traditionally, typically, ultimately, virtually, wholly, widely'.split(', ') ] )


# In[266]:


from collections import defaultdict, Counter
from pprint import pprint
import gzip, sys, math

def read_ngrams():
    # compute distance-bigram
    
    skipBigramDistance = defaultdict(lambda: defaultdict(lambda: Counter()) )
    skipBigramInfo = defaultdict(lambda: defaultdict())
    skipBigramExample = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: [])) )
    for line in sys.stdin:
#     for line in gzip.open('citeseerx.ngms.gz', 'rt'):
        pattern, count = line.split('\t')
        tokens, count = pattern.split(' '), int(count)
        len_ptn = len(tokens)
        
        first, last = tokens[0], tokens[-1]
        skipBigramDistance[first][last][len_ptn-1] += count
        skipBigramDistance[last][first][1-len_ptn] += count
        skipBigramExample[first][last][len_ptn-1].append((pattern, count))
        skipBigramExample[last][first][1-len_ptn].append((pattern, count))

    for head in skipBigramDistance:
        total_freq, variance = 0, 0
        for col in skipBigramDistance[head]:
            values = list(skipBigramDistance[head][col].values())
            freq, avg_f, std = np.sum(values), np.mean(values), np.std(values)
            total_freq += freq
            variance += (avg_f - freq)**2
            
            avg_p = freq/10
            spread = math.sqrt(sum([ (skipBigramDistance[head][col][j] - avg_p)**2/10 for j in range(-5, 6)]))
            skipBigramInfo[head][col] = {'freq': freq, 'avg_f': avg_f, 'std': std, 
                                         'avg_p': avg_p, 'spread': spread}

    return (skipBigramDistance, skipBigramInfo, skipBigramExample)


import numpy as np

if __name__ == '__main__':
    skipBigram, skipBigramInfo, skipBigramExample = read_ngrams()    
    
#     for key in ['separate-v']:
    for key in akl.keys(): 
        N = len(skipBigramInfo[key])
        if N == 0: continue

        avg_f = sum([ info['freq'] for col, info in skipBigramInfo[key].items() ]) / N    
        std = math.sqrt( sum([ (info['freq'] - info['avg_f'])**2 / N for col, info in skipBigramInfo[key].items() ]) )

        remains = filter(lambda x: (skipBigramInfo[key][x[0]]['freq'] - avg_f) / std > 1, skipBigram[key].items())
        remains = filter(lambda x: skipBigramInfo[key][x[0]]['spread'] > 10, remains)

        print("\n" + str(key))
        for token, ctr in remains:
            ctr = max(filter(lambda x: x[1] > skipBigramInfo[key][token]['avg_p'] + math.sqrt(skipBigramInfo[key][token]['spread']), ctr.items()), key=lambda x: x[1])
            print(token, skipBigramInfo[key][token]['freq'], "\t", max(skipBigramExample[key][token][ctr[0]], key=lambda x: x[1]))

