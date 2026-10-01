import { Seo } from '../components/Seo'
import { teamPortraits } from '../data/team'

export const TeamPage = () => (
  <main className="team-page">
    <Seo title="Our Team" description="Meet the people who make M & S Tractor & Equipment a friendly place to find and service a vehicle." />
    <section className="about-hero team-hero" aria-labelledby="team-title">
      <div className="about-hero-copy">
        <h1 id="team-title">Meet the Team.</h1>
        <p>Meet the team behind M &amp; S Tractor &amp; Equipment. We can help with your equipment, parts, and service questions.</p>
      </div>
    </section>
    <section id="team-gallery" className="team-gallery mt-8 px-5 py-8 sm:py-12 lg:mt-10 lg:py-16" aria-label="Our team">
        <div className="mx-auto grid max-w-[1400px] grid-cols-2 gap-x-4 gap-y-7 sm:gap-x-6 sm:gap-y-10 lg:grid-cols-4 lg:gap-x-8 lg:gap-y-12">
          {teamPortraits.map((member, index) => (
            <article key={member.src} className="group overflow-hidden rounded-t-[8px] bg-[var(--color-surface)] shadow-[0_10px_26px_rgba(31,40,33,0.12)]">
              <div className="relative aspect-[4/5] overflow-hidden rounded-t-[8px] bg-[var(--color-border)]">
                <img
                  src={member.src}
                  alt={member.alt}
                  loading={index > 3 ? 'lazy' : 'eager'}
                  className="absolute inset-0 h-full w-full object-cover"
                  style={{ transform: `scale(${member.zoom})`, transformOrigin: `50% ${member.focusY}%` }}
                />
              </div>
              <div className="px-4 py-4 sm:px-5 sm:py-5">
                <h2 className="text-[18px] font-bold uppercase leading-none tracking-[-0.025em] text-[var(--color-primary)] sm:text-[25px] lg:text-[29px]">{member.name}</h2>
                <p className="mt-1 text-[13px] font-medium text-[var(--color-accent)] sm:text-[14px]">{member.title}</p>
              </div>
            </article>
          ))}
        </div>
    </section>
  </main>
)
