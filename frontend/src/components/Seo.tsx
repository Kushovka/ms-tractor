import { useEffect } from 'react'
import { business } from '../data/business'

type SeoProps = {
  title: string
  description: string
  schema?: Record<string, unknown>
  noIndex?: boolean
}

export const Seo = ({ title, description, schema, noIndex = false }: SeoProps) => {
  useEffect(() => {
    document.title = `${title} | ${business.name}`

    let meta = document.querySelector<HTMLMetaElement>('meta[name="description"]')
    if (!meta) {
      meta = document.createElement('meta')
      meta.name = 'description'
      document.head.appendChild(meta)
    }
    meta.content = description

    let robots = document.querySelector<HTMLMetaElement>('meta[name="robots"]')
    const originalRobotsContent = robots?.content
    if (noIndex) {
      if (!robots) {
        robots = document.createElement('meta')
        robots.name = 'robots'
        document.head.appendChild(robots)
      }
      robots.content = 'noindex, follow'
    }

    const existing = document.querySelector('#schema-json')
    existing?.remove()

    if (schema) {
      const script = document.createElement('script')
      script.id = 'schema-json'
      script.type = 'application/ld+json'
      script.textContent = JSON.stringify(schema)
      document.head.appendChild(script)
    }

    return () => {
      if (noIndex && robots) {
        if (originalRobotsContent === undefined) robots.remove()
        else robots.content = originalRobotsContent
      }
    }
  }, [description, noIndex, schema, title])

  return null
}
