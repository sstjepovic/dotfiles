# Prompt Color

PS1="\[$(tput setaf 228)\]\u"; 			# Usuario Amarillo
PS1+="\[$(tput setaf 159)\]@"; 			# @ Celeste
PS1+="\[$(tput setaf 218)\]\h"; 			# Host Rosado
PS1+="\[$(tput setaf 141)\] \W$(tput sgr0)-> "; 	# Directorio actual azul
export PS1;

# End

# Aliases

alias grep='grep --color=auto'
alias ls='exa --group-directories-first'
alias vim='nvim'
alias tree='exa -T'

# End
