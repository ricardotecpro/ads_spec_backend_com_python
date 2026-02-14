from playwright.sync_api import Page, expect

def test_termynal_copy_button(page: Page, start_server):
    """
    Test that the Termynal copy button is injected and visible.
    """
    # Grant clipboard permissions
    page.context.grant_permissions(['clipboard-write', 'clipboard-read'])

    # Navigate to Lesson 01 where we added the Termynal block
    page.goto("http://localhost:8766/01/")

    # Wait for Termynal to be visible
    termynal = page.locator(".termy").first
    expect(termynal).to_be_visible()

    # Check for copy button
    copy_button = termynal.locator(".termynal-copy-button")
    expect(copy_button).to_be_attached()
    
    # Check that it's visible (might need hover, but let's check attachment first)
    # The CSS makes it opacity 0.5 initially, so it should be visible-ish
    # But let's check strict visibility
    expect(copy_button).to_be_visible()

    # Click the button
    copy_button.click()

    # Check for feedback "Copied!" (managed by CSS class .copied showing the span)
    expect(copy_button).to_have_class(r"termynal-copy-button copied")
    
    feedback = copy_button.locator(".termynal-copy-feedback")
    expect(feedback).to_be_visible()
