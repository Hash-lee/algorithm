import sys
sys.setrecursionlimit(10**6)

def solution(p):
    # 올바른 괄호 검증
    def brief(p):
        if p == '': return True
        Q=[0]
        for i in range(len(p)):
            if p[i] == "(": Q.append(p[i])
            else:
                if not Q.pop(): return False
        return True

    # 검사를 재귀로 해서 깊이 초과남
    def div(p, i=0, l=0, r=0):
        if p == '': return ''
        if l != 0 and l == r:
            U, V = p[:i], p[i:]
            if brief(U): return U + div(V)
            else:
                U = (":".join(U)).split(":")
                U.pop(0)
                U.pop()
                for i in range(len(U)):
                    if U[i] == "(": U[i] = ")"
                    else: U[i] = "("
                U = "".join(U)
                return "(" + div(V) + ")" + U
        else:
            if p[i] == "(": return div(p, i+1, l+1, r)
            elif p[i] == ")": return div(p, i+1, l, r+1)
    return div(p)