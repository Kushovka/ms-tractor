import { FaChevronDown } from 'react-icons/fa'

type HeroScrollCueProps = {
  target: string
  label: string
}

export const HeroScrollCue = ({ target, label }: HeroScrollCueProps) => (
  <a className="hero-scroll-cue" href={`#${target}`} aria-label={label}>
    <FaChevronDown aria-hidden="true" />
  </a>
)
